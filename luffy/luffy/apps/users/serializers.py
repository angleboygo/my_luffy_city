from rest_framework import serializers
from .models import User
import re
from django_redis import get_redis_connection

class UserModelSerializer(serializers.ModelSerializer):
    '''
        待校验的数据
          "mobile":this.mobile,
          "password":this.password,
          "password2":this.password2,
          "sms_code":this.sms_code,
    '''
    sms_code=serializers.CharField(label='手机验证码',required=True,allow_blank=False,write_only=True)
    password2=serializers.CharField(label='确认密码',required=True,allow_blank=False,write_only=True)
    token=serializers.CharField(label='jwt',read_only=True)

    class Meta:
        model=User
        fields=('id','sms_code','password','password2','token','mobile')
        extra_kwargs={
            'password':{'write_only':True},
            'id':{'read_only':True}
        }

    def validate_mobile(self,value):
        '验证手机'
        if not re.match(r'^1[345789]\d{9}',value):
            raise serializers.ValidationError('手机格式不对')
        try:
            User.objects.get(mobile=value)
            raise serializers.ValidationError('该用户已注册')
        except:
            pass
        return value

    def validate(self, data):
        '验证密码是否一致'
        # print('dict',data)
        password=data.get('password')
        password2=data.get('password2')
        if len(password)<6:
            raise serializers.ValidationError('密码太短了,不安全')

        if password!=password2:
            raise serializers.ValidationError('密码和确认密码不一致')

        '''验证短信验证码'''
        mobile=data.get('mobile')
        sms_code=data.get('sms_code')


        #从redis中取验证码
        redis=get_redis_connection('sms_code')
        #注意,在redis中保存的数据德格式,最终都是bytes类型的字符串,
        print('-----------------',type(redis.get('sms_%s'%mobile)))
        redis_sms_code=redis.get('sms_%s'%mobile).decode()
        #把redis中的验证码和客户端提交的验证码进行匹配
        if not (redis_sms_code and redis_sms_code==sms_code):
            raise serializers.ValidationError('手机验证码无效!')


        return data

    def create(self,validated_data):
        '删除一些不需要保存到数据库里面的字段'
        del validated_data['password2']
        del validated_data['sms_code']

        user=super().create(validated_data)
        user.save()
        return user


