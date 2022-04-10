from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from clsMan.models import ClassTable
from stdMan.models import StudTable
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return render(request, 'manager/class.html', locals())
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def getData(request):
    dlen = 0
    jsonData = []
    if request.method == 'POST':
        QuerySet = ClassTable.objects.all()
        dlen = len(QuerySet)
    for row in QuerySet:
        result = {}
        result['num'] = row.clsID
        result['name'] = row.clsName
        result['desc'] = row.clsDesc
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
def delCls(request):
    try:
        data =request.POST['data'].split(',')
        print(data)
        for i in data:
            ClassTable.objects.get(clsID=i).delete()
        return HttpResponse("ok")
    except:
        return HttpResponse('fail')



@csrf_exempt
def addCls(request):
    try:
        if request.method == 'POST':
            num = request.POST['num']
            name = request.POST['name']
            desc = request.POST['desc']

        query = ClassTable.objects.filter(clsID=num)
        dlen = len(query)
        if(dlen>0):
            return HttpResponse('have')
        else:
            clsinfo = ClassTable.objects.create(
                clsID=num,
                clsName=name,
                clsDesc=desc,
            )
            return HttpResponse("ok")
    except:
        return HttpResponse("fail")

@csrf_exempt
def editCls(request):
    try:
        if request.method == 'POST':
            num = request.POST['num']
            name = request.POST['name']
            desc = request.POST['desc']

        query = ClassTable.objects.filter(clsID=num)
        #dlen = len(query)
        t = ClassTable.objects.get(clsID=num)
        t.clsName=name
        t.clsDesc=desc
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




@csrf_exempt
def classDetail(request):
    class_id = request.GET.get('class_id')
    class_name = ClassTable.objects.get(clsID=class_id).clsName
    return render(request, 'manager/class_detail.html', locals())

@csrf_exempt
def getDetailData(request):
    '''获取班级学生详细数据'''
    dlen = 0
    jsonData = []
    classID = request.GET.get('class_id')
    if request.method == 'POST':
        QuerySet = StudTable.objects.filter(classID_id=classID)
        dlen = len(QuerySet)
    for row in QuerySet:
        result = {}
        result['num'] = row.stuID
        result['ch_name'] = row.stuChName
        result['en_name'] = row.stuEnName
        result['republic'] = row.stuRepublic
        #result['class'] = row.classID_id
        result['birth'] = row.stuBirthday
        result['sex'] = row.stuSex
        result['Desc'] = row.stuDesc
        result['contact'] = row.stuContact
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
def delStud(request):
    '''删除班级学生操作'''
    try:
        data =request.POST['data'].split(',')
        print(data)
        for i in data:
            StudTable.objects.get(stuID=i).delete()
        return HttpResponse("ok")
    except:
        return HttpResponse('fail')


@csrf_exempt
def addStud(request):
    '''添加班级学生操作'''
    try:
        if request.method == 'POST':
            num = request.POST['num']
            ch_name = request.POST['ch_name']
            en_name = request.POST['en_name']
            sex = request.POST['sex']
            contact = request.POST['contact']
            birth = request.POST['birth']
            # 处理日期格式化带来的问题
            if birth != '':
                birth = datetime.strptime(birth, "%d/%m/%Y").strftime("%Y-%m-%d")
            else: #当birth为空字符串时,需要重新赋值为None才能写进数据库
                birth = None
            republic = request.POST['republic']
            class_ = request.POST['class']

        query = StudTable.objects.filter(stuID=num)
        dlen = len(query)
        if(dlen>0):
            return HttpResponse('have')
        else:
            studinfo = StudTable.objects.create(
                stuID=num,
                stuChName=ch_name,
                stuEnName=en_name,
                stuSex=sex,
                stuRepublic= republic,
                stuContact=contact,
                stuBirthday=birth,
                classID_id=class_
            )
            return HttpResponse("ok")
    except:
        return HttpResponse("fail")


