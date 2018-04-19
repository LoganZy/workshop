from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    '''
    用户表，新增字段如下
    '''
    GENFER_CHOICES = (
        ('male',u'男'),
        ('female',u'女'),
    )
    # 用户注册是我们需要新建user_profile 但是我们只有手机号
    name = models.CharField(max_length=30,null=True,blank=True,verbose_name='姓名')
    # 保存出生日期，年龄通过出生日期推算
    brithday = models.DateField(null=True,blank=True,verbose_name='出生年月')
    gender = models.CharField(max_length=6,choices=GENFER_CHOICES,default='female',verbose_name='性别')
    mobile = models.CharField(max_length=11,verbose_name='电话'),
    email = models.EmailField(max_length=100,null=True,blank=True,verbose_name='邮箱')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class VerifyCode(models.Model):
    '''
    短信验证码，回填短信验证码验证，可以保存在redis
    '''
    code = models.CharField(max_length=100,verbose_name='验证码')
    mobile = models.CharField(max_length=11,verbose_name='电话')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code