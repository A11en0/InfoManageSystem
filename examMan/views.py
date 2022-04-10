from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from examMan.models import ExamTable, EaxmType
from teacherMan.models import TeacherTable
from stdMan.models import StudTable
from clsMan.models import ClassTable
from courseMan.models import CourseTable, ChooseCourse
from studscore.models import StudScoreTable
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return render(request, 'manager/exam.html', locals())
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def getData(request):
    dlen = 0
    jsonData = []
    if request.method == 'POST':
        QuerySet = ExamTable.objects.all()
        dlen = len(QuerySet)
    for row in QuerySet:
        result = {}
        result['id'] = row.examID
        result['name'] = row.examName
        result['time'] = row.examTime.strftime("%Y-%m-%d %H:%M")
        result['type'] = row.examType.type
        result['class'] = row.classID.clsName
        result['course'] =row.courseID.courseName
        result['desc'] = row.examDesc

        jsonData.append(result)

    pagesize = request.POST['pageSize']
    offset = request.POST['offset']

    mydata = {
    "total": dlen,
    "rows": jsonData[int(offset):int(pagesize)+int(offset)]
    }
    return JsonResponse(mydata)


@csrf_exempt
def delExam(request):
    try:
        data =request.POST['data'].split(',')
        print(data)
        for i in data:
            ExamTable.objects.get(examID=i).delete()
        return HttpResponse("ok")
    except:
        return HttpResponse('fail')


@csrf_exempt
def addExam(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            time = request.POST['time']
            type = request.POST['type']
            course = request.POST['course']
            class_ = request.POST['class_']
            desc = request.POST['desc']

            query = ExamTable.objects.filter(examName=name)
            dlen = len(query)
            if(dlen>0):
                return HttpResponse('have')

            Examinfo = ExamTable.objects.create(
                examName=name,
                examDesc=desc,
                courseID_id=course,
                examTime=time,
                examType_id=type,
                classID_id=class_,
            )
            return HttpResponse("ok")
    except:
        return HttpResponse("fail")

@csrf_exempt
def editScore(request):
    try:
        if request.method == 'POST':
            num = request.POST['num']
            score = request.POST['score']
            #courseID = request.POST['courseID']
            examID = request.POST['examID']
            try:
                t = StudScoreTable.objects.get(stud=num, examID_id=examID)
                t.stuScore = score
                t.save()
            except:
                StudScoreTable.objects.create(
                    examID_id=examID, stud_id=num, stuScore=score
                )

        return JsonResponse({'status': 'success'}, safe=False)
    except:
        return JsonResponse({'status': 'fail'}, safe=False)

@csrf_exempt
def entryScore(request):
    if request.user.is_authenticated():
        courseID = request.GET.get('course_id')
        classID = request.GET.get('class_id')
        examID = request.GET.get('exam_id')
        dlen = 0
        jsonData = []
        if request.method == 'POST':
            courseID = request.GET.get('courseID')
            #classID = request.GET.get('classID')
            examID = request.GET.get('exam_id')
            #students = ChooseCourse.objects.filter(courseID_id=courseID,studID__classID=classID)
            exam = ExamTable.objects.get(examID=examID)
            students = StudTable.objects.filter(classID_id=exam.classID_id)
            dlen = len(students)
            for row in students:
                result = {}
                try:
                    score = StudScoreTable.objects.get(stud=row.stuID, examID_id=exam.examID).stuScore
                    result['num'] = row.stuID
                    result['ch_name'] = row.stuChName
                    result['score'] = score
                except:
                    result['num'] = row.stuID
                    result['ch_name'] = row.stuChName
                    result['score'] = None

                jsonData.append(result)

                pagesize = request.POST['pageSize']
                offset = request.POST['offset']

                mydata = {
                    "total": dlen,
                    "rows": jsonData[int(offset):int(pagesize) + int(offset)]
                }

            return JsonResponse(mydata)

        return render(request, 'manager/entryscore.html', locals())
    else:
        return HttpResponseRedirect('/login')

def select_course(request):
    jsondata = []
    query = CourseTable.objects.all()
    for row in query:
        result = {}
        result['courseID'] = row.courseID
        result['courseName'] = row.courseName
        jsondata.append(result)
    mydata = {'jsondata':jsondata}
    return JsonResponse(mydata)

def select_class(request):
    jsondata = []
    query = ClassTable.objects.all()
    for row in query:
        result = {}
        result['classID'] = row.clsID
        result['className'] = row.clsName
        jsondata.append(result)
    mydata = {'jsondata':jsondata}
    return JsonResponse(mydata)

def select_type(request):
    jsondata = []
    query = EaxmType.objects.all()
    for row in query:
        result = {}
        result['typeID'] = row.id
        result['typeName'] = row.type
        jsondata.append(result)
    mydata = {'jsondata':jsondata}
    return JsonResponse(mydata)

