from django.db import models
from clsMan.models import ClassTable

# Create your models here.
class TeacherTable(models.Model):
    techID = models.CharField(max_length=100, primary_key=True, verbose_name="ID")
    techName = models.CharField(max_length=100,verbose_name="姓名")
    techSex = models.CharField(max_length=10,blank=True,null=True,choices=(('男', '男',),('男', '女')), default='男',verbose_name="性别")
    techBirthday = models.DateField(verbose_name="出生日期",blank=True,null=True)
    techDesc = models.CharField(max_length=100,blank=True,null=True,verbose_name="个人描述")
    techContact = models.CharField(max_length=100,blank=True,null=True,verbose_name="联系方式")

    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name
        ordering = ['techID', 'techName']

    def __str__(self):
        return self.techName