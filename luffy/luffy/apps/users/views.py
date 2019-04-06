import json
import random

from django_redis import get_redis_connection

from rest_framework.response import Response
from rest_framework.views import APIView
from luffy.libs.geetest import GeetestLib

# Create your views here.

class VerifyCode(APIView):
    gt = None
    """验证码类"""
    def get(self,request):
        """获取验证码"""
        user_id = random.randint(1, 100)
        APP_ID = "884b024377529d6ba4d2f07d227879df"
        APP_KEY = "28e7f92b7c66f718d65ede8feb26f477"
        gt = GeetestLib(APP_ID,APP_KEY)

        status = gt.pre_process(user_id,JSON_FORMAT=0, ip_address="http://localhost:8080")
        request.session[gt.GT_STATUS_SESSION_KEY] = status
        print("session=%s" % status )
        request.session["user_id"] = user_id
        data = gt.get_response_str()
        return Response(data)

    def post(self,request):
        result = {"status": "success", "code": 111}
        return (result)


################用户验证
from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserModelSerializer
class UserAPIview(CreateAPIView):
    '用户管理'
    queryset=User.objects.all()
    serializer_class = UserModelSerializer


################sms
from rest_framework import status
from luffy.libs.yuntongxun.sms import CCP
from django_redis import get_redis_connection
class SMSCodeAPIView(APIView):
    def get(self, request):
        #通过字符串获取手机号码
        mobile=request.query_params.get('mobile')
        # 2. 发送短信之前验证码验证一下手机号码
        try:
            User.objects.get(mobile=mobile)
            return Response({'msg':'当前手机号被注册过'},status=status.HTTP_400_BAD_REQUEST)
        except:
            pass
        redis=get_redis_connection('sms_code')
        if redis.get('time_%s'%mobile):
            return Response({'message':'当前手机号,已经在一分钟内发送过短信'},status.HTTP_400_BAD_REQUEST)

        # 3. 使用手机号码发送短信验证码
        # 生成一个短信验证码
        sms_code = "%04d" % random.randint(55, 9999)
        ccp = CCP()
        result = ccp.send_template_sms(mobile, [sms_code, "5分钟"], 1)
        if result==0:
            #发送短信成功,保存短信验证信息到redis数据库中
            #开启管道
            pl = redis.pipeline()
            pl.multi() #表示接下来会在管道中执行多条命令

            #setex(变量名,有效期[秒],值)
            SMS_EXPIRE_TIME = 5 * 60  # 短信验证码的有效期
            SMS_TIMES = 60  # 短信发送的间隔时间

            #把原来立即执行的命令放置到管道中
            pl.setex('sms_%s'%mobile,SMS_EXPIRE_TIME,sms_code)
            pl.setex('times_%s'%mobile,SMS_TIMES,1)

            #统一执行管道中的命令
            pl.execute()

        # 4. 响应数据给客户端
        return Response({"message": result}, status=status.HTTP_200_OK)


    # def post(self,request):
    #     pass


