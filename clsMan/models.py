from django.db import models

# Create your models here.
class ClassTable(models.Model):
    clsID = models.CharField(max_length=100,primary_key=True,verbose_name="班级编号")
    clsName = models.CharField(max_length=100,verbose_name="班级名称")
    clsDesc = models.CharField(max_length=100,verbose_name="班级描述",blank=True)

    class Meta:
        verbose_name = '班级信息'
        verbose_name_plural = verbose_name
        ordering = ['clsID', 'clsName']

    def __str__(self):
        return self.clsName