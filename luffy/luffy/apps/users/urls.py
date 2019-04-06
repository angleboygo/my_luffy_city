from django.urls import path,re_path
#引入jwt用户验证
from rest_framework_jwt.views import  obtain_jwt_token
from . import views

urlpatterns=[
    path(r'login/',obtain_jwt_token),
    path(r'verify/',views.VerifyCode.as_view()),
    path(r'user/',views.UserAPIview.as_view()),
    path(r'sms/',views.SMSCodeAPIView.as_view()),

]