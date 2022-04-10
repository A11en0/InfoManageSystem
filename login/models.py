from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 用户(User)模型
# 采用的继承方式扩展用户信息

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True,null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')

    class Meta:
        # verbose_name：数据库表名名称，这里表名称为“用户”
        verbose_name = '系统用户'
        # verbose_name_plural：人类可读的单复数名称，这里“用户”复数名称为“用户”
        verbose_name_plural = verbose_name
        # ordering：如排序选项，这里以id降序来排序
        ordering = ['-id']

    # 对象的字符串表达式(unicode格式)
    def __str__(self):
        return self.username

