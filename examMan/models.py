from django.db import models
from clsMan.models import ClassTable
from teacherMan.models import TeacherTable
from courseMan.models import CourseTable
# Create your models here.

class EaxmType(models.Model):
    type = models.CharField(max_length=100, verbose_name="考试类型")

    class Meta:
        verbose_name = '考试类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type

class ExamTable(models.Model):
    examID = models.AutoField(max_length=100,primary_key=True)
    examName = models.CharField(max_length=100, verbose_name="考试名称")
    examTime = models.DateTimeField(max_length=100, verbose_name="考试时间",blank=True,null=True)
    examType = models.ForeignKey(EaxmType, max_length=100, verbose_name="考试类型", on_delete=models.CASCADE)
    examDesc = models.CharField(max_length=100, verbose_name="备注", blank=True, null=True,)
    courseID = models.ForeignKey(CourseTable, max_length=100, verbose_name="考试科目", on_delete=models.CASCADE)
    classID = models.ForeignKey(ClassTable, max_length=100, blank=True,null=True, verbose_name="考试班级", on_delete=models.CASCADE)

    class Meta:
        verbose_name = '考试信息'
        verbose_name_plural = verbose_name
        ordering = ['examID', 'examName']

    def __str__(self):
        return self.examName
