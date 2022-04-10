from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from studscore.models import StudScoreTable
from clsMan.models import ClassTable
from courseMan.models import CourseTable
from stdMan.models import StudTable
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.

def main(request):
    return render(request, 'manager/studscore.html', locals())


'''
@csrf_exempt
def getData(request):
    dlen = 0
    jsonData = []

    if request.method == 'POST':
        if request.POST.get('filter') == None:
            QuerySet = StudScoreTable.objects.all()
            dlen = len(QuerySet)

            for row in QuerySet:
                result = {}
                result['id'] = row.scoreID
                result['num'] = row.stud.stuID
                result['ch_name'] = row.stud.stuChName
                result['en_name'] = row.stud.stuEnName
                result['course'] = row.examID.courseID.courseName
                result['score'] = row.stuScore
                jsonData.append(result)

            pagesize = request.POST['pageSize']
            offset = request.POST['offset']
            mydata = {
                "total": dlen,
                "rows": jsonData[int(offset):int(pagesize) + int(offset)]
            }

            return JsonResponse(mydata)

        else:
            num = request.POST['num']
            class_id = request.POST['class_id']
            course_id = request.POST['course_id']
            if num != '':
                QuerySet = StudScoreTable.objects.filter(stud_id=num)
            if (class_id != ''):
                QuerySet = StudScoreTable.objects.filter(stud__classID=class_id)
            if (course_id != ''):
                QuerySet = StudScoreTable.objects.filter(examID__courseID=course_id)
            if (num != '' and class_id != ''):
                QuerySet = StudScoreTable.objects.filter(stud_id=num, stud__classID=class_id)
            if (num != '' and course_id != ''):
                QuerySet = StudScoreTable.objects.filter(stud_id=num, examID__courseID=course_id)
            if (class_id != '' and course_id != ''):
                QuerySet = StudScoreTable.objects.filter(stud__classID=class_id, examID__courseID=course_id)
            if (num != '' and class_id != '' and course_id != ''):
                QuerySet = StudScoreTable.objects.filter(stud_id=num,stud__classID=class_id, examID__courseID=course_id)
            if (num == '' and class_id == '' and course_id == ''):
                QuerySet = StudScoreTable.objects.all()
            dlen = len(QuerySet)

            for row in QuerySet:
                result = {}
                result['id'] = row.scoreID
                result['num'] = row.stud.stuID
                result['ch_name'] = row.stud.stuChName
                result['en_name'] = row.stud.stuEnName
                result['course'] = row.examID.courseID.courseName
                result['score'] = row.stuScore
                jsonData.append(result)

            pagesize = request.POST['pageSize']
            offset = request.POST['offset']
            mydata = {
            "total": dlen,
            "rows": jsonData[int(offset):int(pagesize)+int(offset)]
            }

            return JsonResponse(mydata)
'''

@csrf_exempt
def getData(request):
    '''获取数据'''
    dlen = 0
    jsonData = []

    if request.method == 'POST':
        num = request.POST['num']
        class_id = request.POST['class_id']
        course_id = request.POST['course_id']
        if (num == '' and class_id == '' and course_id == ''):
            #QuerySet = StudScoreTable.objects.all()
            QuerySet = StudScoreTable.objects.all()

        else:
            if num != '':
                QuerySet = StudScoreTable.objects.filter(stud_id=num)
            if (class_id != ''):
                QuerySet = StudScoreTable.objects.filter(stud__classID=class_id)
            if (course_id != ''):
                QuerySet = StudScoreTable.objects.filter(examID__courseID=course_id)
            if (num != '' and class_id != ''):
                QuerySet = StudScoreTable.objects.filter(stud_id=num, stud__classID=class_id)
            if (num != '' and course_id != ''):
                QuerySet = StudScoreTable.objects.filter(stud_id=num, examID__courseID=course_id)
            if (class_id != '' and course_id != ''):
                QuerySet = StudScoreTable.objects.filter(stud__classID=class_id, examID__courseID=course_id)
            if (num != '' and class_id != '' and course_id != ''):
                QuerySet = StudScoreTable.objects.filter(stud_id=num,stud__classID=class_id, examID__courseID=course_id)

        for row in QuerySet:
            result = {}
            result['id'] = row.scoreID
            result['num'] = row.stud.stuID
            result['ch_name'] = row.stud.stuChName
            result['en_name'] = row.stud.stuEnName
            result['course'] = row.examID.courseID.courseName
            result['score'] = row.stuScore
            jsonData.append(result)
        dlen = len(QuerySet)
        pagesize = request.POST['pageSize']
        offset = request.POST['offset']
        mydata = {
        "total": dlen,
        "rows": jsonData[int(offset):int(pagesize) + int(offset)]
        }

        return JsonResponse(mydata)

@csrf_exempt
def delScore(request):
    '''删除操作'''
    try:
        data =request.POST['data'].split(',')
        print(data)
        for i in data:
            StudScoreTable.objects.get(scoreID=i).delete()
        return HttpResponse("ok")
    except:
        return HttpResponse('fail')


@csrf_exempt
def addScore(request):
    '''添加操作'''
    try:
        if request.method == 'POST':
            num = request.POST['num']
            score = request.POST['score']
            course = request.POST['course']

        query = StudScoreTable.objects.filter(course=course, stud=num)
        dlen = len(query)
        if(dlen>0):
            return HttpResponse('have')
        else:
            # stud studscore course
        #s = StudTable.objects.create(stuID=num)
        #c = CourseTable.objects.create(courseID=course)

        #s = StudTable.objects.get(stuID=num)
        #print(type(s))
        #c = CourseTable.objects.get(courseID=course)
            StudScoreTable.objects.create(
                stud_id=num, stuScore=score, course_id=course
            )
            return HttpResponse("ok")
    except:
        return HttpResponse("fail")

@csrf_exempt
def editScore(request):
    '''添加操作'''
    try:
        if request.method == 'POST':
            num = request.POST['num']
            ch_name = request.POST['ch_name']
            en_name = request.POST['en_name']
            sex = request.POST['sex']
            contact = request.POST['contact']
            birth = request.POST['birth']
            republic = request.POST['republic']
            class_ = request.POST['class']

        query = StudScoreTable.objects.filter(stuID=num)
        query_class_id = ClassTable.objects.get(clsName=class_)
        dlen = len(query)
        #if(dlen>0):
        #    return HttpResponse('have')
        #else:
        t = StudScoreTable.objects.get(stuID=num)
        #stuID=num,
        t.stuChName=ch_name
        t.stuEnName=en_name
        t.stuSex=sex
        t.stuRepublic= republic
        t.stuContact=contact
        t.stuBirthday=birth
        t.classID_id=query_class_id.clsID
        t.save()
        return JsonResponse({'status':'success'},safe=False)
    except:
        return JsonResponse({'status':'fail'},safe=False)

def fillSelect(request):
    jsondata = []
    query = CourseTable.objects.all()
    for row in query:
        result = {}
        result['courseID'] = row.courseID
        result['courseName'] = row.courseName
        jsondata.append(result)
    mydata = {'jsondata':jsondata}
    return JsonResponse(mydata)

def fillNum(request):
    jsondata = []
    query = StudTable.objects.all()
    for row in query:
        result = {}
        result['stuID'] = row.stuID
        jsondata.append(result)
    mydata = {'jsondata':jsondata}
    return JsonResponse(mydata)

def fillClass(request):
    jsondata = []
    query = ClassTable.objects.all()
    for row in query:
        result = {}
        result['classID'] = row.clsID
        result['className'] = row.clsName
        jsondata.append(result)
    mydata = {'jsondata':jsondata}
    return JsonResponse(mydata)




