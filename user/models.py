from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.
class UserProfile(AbstractUser):
    register_time = models.DateTimeField(default=datetime.now, verbose_name='注册时间')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class EmailVerify(models.Model):
    email = models.CharField(max_length=100, verbose_name='邮箱')
    code = models.CharField(max_length=20, verbose_name='验证码')
    send_type = models.CharField(choices=(('register', '注册'), ('update', '修改')), max_length=20, verbose_name='类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = verbose_name

