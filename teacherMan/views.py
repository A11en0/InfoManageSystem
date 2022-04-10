from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from teacherMan.models import TeacherTable

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return render(request, 'manager/teacher.html', locals())
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def getData(request):
    dlen = 0
    jsonData = []
    if request.method == 'POST':
        QuerySet = TeacherTable.objects.all()
        dlen = len(QuerySet)
    for row in QuerySet:
        result = {}
        result['num'] = row.techID
        result['name'] = row.techName
        result['sex'] = row.techSex
        result['Desc'] = row.techDesc
        result['contact'] = row.techContact

        jsonData.append(result)

    pagesize = request.POST['pageSize']
    offset = request.POST['offset']

    mydata = {
    "total": dlen,
    "rows": jsonData[int(offset):int(pagesize)+int(offset)]
    }

    return JsonResponse(mydata)


@csrf_exempt
def delTech(request):
    try:
        data =request.POST['data'].split(',')
        print(data)
        for i in data:
            TeacherTable.objects.get(techID=i).delete()
        return HttpResponse("ok")
    except:
        return HttpResponse('fail')

@csrf_exempt
def addTech(request):
    try:
        if request.method == 'POST':
            num = request.POST['num']
            name = request.POST['name']
            sex = request.POST['sex']
            contact = request.POST['contact']

        query = TeacherTable.objects.filter(techID=num)
        dlen = len(query)
        if(dlen>0):
            return HttpResponse('have')
        else:
            techinfo = TeacherTable.objects.create(
                techID=num,
                techName=name,
                techSex=sex,
                techContact=contact,
            )
            return HttpResponse("ok")
    except:
        return HttpResponse("fail")

@csrf_exempt
def editTech(request):
    try:
        if request.method == 'POST':
            num = request.POST['num']
            name = request.POST['name']
            sex = request.POST['sex']
            contact = request.POST['contact']
            #birth = request.POST['birth']
            # 处理日期格式化带来的问题
            #if birth == '':
            #    birth = None

        query = TeacherTable.objects.filter(techID=num)
        #query_class_id = ClassTable.objects.get(className=class_)
        dlen = len(query)
        #if(dlen>0):
        #    return HttpResponse('have')
        #else:
        t = TeacherTable.objects.get(techID=num)
#stuID=num,
        t.techName=name
        t.techSex=sex
        t.techContact=contact
        #.techBirthday = birth
        t.save()
        return JsonResponse({'status':'success'},safe=False)
    except:
        return JsonResponse({'status':'fail'},safe=False)

def fillSelect(request):
    jsondata = []
    query = ClassTable.objects.all()
    for row in query:
        result = {}
        result['classID'] = row.classID
        result['className'] = row.className
        jsondata.append(result)
    mydata = {'jsondata':jsondata}
    return JsonResponse(mydata)



