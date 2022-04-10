from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from stdMan.models import StudTable
from clsMan.models import ClassTable
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return render(request, 'manager/student.html', locals())
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def getData(request):
    '''获取数据'''
    dlen = 0
    jsonData = []
    if request.method == 'POST':
        QuerySet = StudTable.objects.all()
        dlen = len(QuerySet)
    for row in QuerySet:
        result = {}
        result['num'] = row.stuID
        result['ch_name'] = row.stuChName
        result['en_name'] = row.stuEnName
        result['republic'] = row.stuRepublic
        result['class'] = row.classID_id
        result['birth'] = row.stuBirthday
        result['sex'] = row.stuSex
        result['Desc'] = row.stuDesc
        result['contact'] = row.stuContact
        jsonData.append(result)
    #mydata = {'total': dlen, 'rows': jsonData}

#   return HttpResponse(json.dumps(mydata))
    pagesize = request.POST['pageSize']
    offset = request.POST['offset']

    '''
    rows = [
        {"id": 1, "name": "sallency", "age": 26},
        {"id": 1, "name": "sallency", "age": 22},
        {"id": 1, "name": "sallency", "age": 24},
    ]
    '''

    mydata = {
    "total": dlen,
    "rows": jsonData[int(offset):int(pagesize)+int(offset)]
    }

    return JsonResponse(mydata)

@csrf_exempt
def delStud(request):
    '''删除操作'''
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
    '''添加操作'''
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

@csrf_exempt
def editStud(request):
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

        query = StudTable.objects.filter(stuID=num)
        #query_class_id = ClassTable.objects.get(clsName=class_)
        dlen = len(query)

        t = StudTable.objects.get(stuID=num)

        t.stuChName=ch_name
        t.stuEnName=en_name
        t.stuSex=sex
        t.stuRepublic= republic
        t.stuContact=contact
        t.stuBirthday=birth
        t.classID_id=class_
        t.save()
        return JsonResponse({'status':'success'},safe=False)
    except:
        return JsonResponse({'status':'fail'},safe=False)

def fillSelect(request):
    jsondata = []
    query = ClassTable.objects.all()
    for row in query:
        result = {}
        result['classID'] = row.clsID
        result['className'] = row.clsName
        jsondata.append(result)
    mydata = {'jsondata':jsondata}
    return JsonResponse(mydata)




