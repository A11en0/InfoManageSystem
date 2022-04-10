from django.db import models
from clsMan.models import ClassTable
from teacherMan.models import TeacherTable
from stdMan.models import StudTable
# Create your models here.

class CourseTable(models.Model):
    courseID = models.AutoField(max_length=100,primary_key=True,verbose_name="课程ID")
    courseName = models.CharField(max_length=100,verbose_name="课程名称")
    courseDesc = models.CharField(max_length=100,verbose_name="课程描述",blank=True)
    classID = models.ForeignKey(ClassTable,max_length=100,blank=True,null=True, on_delete=models.CASCADE)
    teacherID = models.ForeignKey(TeacherTable,max_length=100,blank=True,null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name
        ordering = ['courseID', 'courseName']

    def __str__(self):
        return self.courseName

class ChooseCourse(models.Model):
    studID = models.ForeignKey(StudTable, verbose_name="学号", on_delete=models.CASCADE)
    courseID = models.ForeignKey(CourseTable, verbose_name="课程编号", on_delete=models.CASCADE)

    class Meta:
        verbose_name = '选课信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.studID.stuChName
