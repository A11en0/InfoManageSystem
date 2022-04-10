from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from courseMan.models import CourseTable
from teacherMan.models import TeacherTable
from clsMan.models import ClassTable
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return render(request, 'manager/course.html', locals())
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def getData(request):
    dlen = 0
    jsonData = []
    if request.method == 'POST':
        QuerySet = CourseTable.objects.all()
        dlen = len(QuerySet)
    for row in QuerySet:
        result = {}
        result['num'] = row.courseID
        result['name'] = row.courseName
        result['desc'] = row.courseDesc
        result['class'] = row.classID_id
        result['teacher'] =row.teacherID_id

        jsonData.append(result)
    #mydata = {'total': dlen, 'rows': jsonData}

#   return HttpResponse(json.dumps(mydata))
    pagesize = request.POST['pageSize']
    offset = request.POST['offset']


    mydata = {
    "total": dlen,
    "rows": jsonData[int(offset):int(pagesize)+int(offset)]
    }

    return JsonResponse(mydata)

@csrf_exempt
def delCourse(request):
    try:
        data =request.POST['data'].split(',')
        print(data)
        for i in data:
            CourseTable.objects.get(courseID=i).delete()
        return HttpResponse("ok")
    except:
        return HttpResponse('fail')


@csrf_exempt
def addCourse(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            desc = request.POST['desc']
            class_ = request.POST['class_']
            teacher = request.POST['teacher']

        #query = CourseTable.objects.filter(courseName=name)
        #dlen = len(query)
        #if(dlen>0):
        #    return HttpResponse('have')
        #else:

            Courseinfo = CourseTable.objects.create(
                courseName=name,
                courseDesc=desc,
                classID_id=class_,
                teacherID_id = teacher
            )
            return HttpResponse("ok")
    except:
        return HttpResponse("fail")

@csrf_exempt
def editCourse(request):
    try:
        if request.method == 'POST':
            num = request.POST['num']
            name = request.POST['name']
            desc = request.POST['desc']
            class_ = request.POST['class']
            teacher = request.POST['teacher']

        query = CourseTable.objects.filter(courseID=num)
        t = CourseTable.objects.get(courseID=num)
        t.courseName = name
        t.courseDesc = desc
        t.classID_id = class_
        t.teacherID_id = teacher
        t.save()
        return JsonResponse({'status': 'success'}, safe=False)
    except:
        return JsonResponse({'status': 'fail'}, safe=False)

def select_teacher(request):
    jsondata = []
    query = TeacherTable.objects.all()
    for row in query:
        result = {}
        result['teacherID'] = row.techID
        result['teacherName'] = row.techName
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


