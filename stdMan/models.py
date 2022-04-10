from django.db import models
from clsMan.models import ClassTable

# Create your models here.
class StudTable(models.Model):
    stuID = models.CharField(max_length=100, primary_key=True, verbose_name="学号")
    stuChName = models.CharField(max_length=100,verbose_name="中文名")
    stuEnName = models.CharField(max_length=100,verbose_name="英文名")
    stuRepublic = models.CharField(max_length=100,blank=True,null=True,verbose_name="国籍")
    #stuAge = models.CharField(max_length=100,blank=True,null=True,verbose_name="年龄")
    stuSex = models.CharField(max_length=10,blank=True,null=True,choices=(('男', 'male',),('女', 'famale')), default='male',verbose_name="性别")
    stuBirthday = models.DateField(verbose_name="出生日期",blank=True,null=True)
    stuDesc = models.CharField(max_length=100,blank=True,null=True,verbose_name="个人描述")
    stuContact = models.CharField(max_length=100,blank=True,null=True,verbose_name="联系方式")
    classID = models.ForeignKey(ClassTable, verbose_name="班级编号",blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name
        ordering = ['stuID', 'stuEnName']

    def __str__(self):
        return self.stuEnName
