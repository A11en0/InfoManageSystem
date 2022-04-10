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
        return render(request, 'student/scorequery.html', locals())
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def getData(request):
    dlen = 0
    jsonData = []
    if request.method == 'POST':
        QuerySet = StudScoreTable.objects.all()
        dlen = len(QuerySet)
    for row in QuerySet:
        result = {}
        result['name'] = row.examID.courseID.courseName
        result['score'] = row.stuScore

        jsonData.append(result)
    #mydata = {'total': dlen, 'rows': jsonData}
    pagesize = request.POST['pageSize']
    offset = request.POST['offset']

    mydata = {
    "total": dlen,
    "rows": jsonData[int(offset):int(pagesize)+int(offset)]
    }

    return JsonResponse(mydata)
