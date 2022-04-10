from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout, login, authenticate
from login.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password

# Create your views here.

@csrf_exempt
def do_register(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            #'username': username, 'password': password, 're_password': re_pasw, 'contact': contact}
            is_exist = User.objects.filter(username__exact=username)
            if is_exist:
                return HttpResponse('exist')
            user = User.objects.create(
                username=username,
                password=make_password(password),
            )
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
            login(request, user)
            #return redirect(request.POST.get('source_url'))
            return HttpResponse('ok')
    except:
        return HttpResponseRedirect('register')
    return render(request, '../templates/register.html', locals())

@csrf_exempt
def do_login(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password) # 判断是否存在用户
            if user is not None:
                user.backend = 'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
                login(request, user)



                return HttpResponse('ok')
            else:
                return HttpResponse('fail')
    except:
        return HttpResponseRedirect('login')
    return render(request, '../templates/login.html', locals())

def register_success(res):
    return render(res, '../templates/register_success.html', locals())

# 注销
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        pass
    return HttpResponseRedirect('/login')
