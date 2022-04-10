from django.db import models
from clsMan.models import ClassTable
from stdMan.models import StudTable
from courseMan.models import CourseTable
from examMan.models import ExamTable
# Create your models here.

class StudScoreTable(models.Model):
    scoreID = models.AutoField(primary_key=True)
    examID = models.ForeignKey(ExamTable,verbose_name="考试ID", default='', on_delete=models.CASCADE)
    stud = models.ForeignKey(StudTable,verbose_name="学号", on_delete=models.CASCADE)
    stuScore = models.CharField(max_length=100,verbose_name="成绩", default="")
    #course = models.ForeignKey(CourseTable,verbose_name="课程编号", default="")

    class Meta:
        verbose_name = '学生成绩'
        verbose_name_plural = verbose_name
        ordering = ['stud', 'stuScore']

