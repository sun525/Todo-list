from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# 登录
def user_login(request):
    '''
    如果是Get请求,返回登录页面;
    如果是Post请求,验证登录数据
    :param request:
    :return:
    '''

    # 反爬虫
    # user_agent = request.META.get()
    msg = None
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # 保存登录状态到会话中
            login(request, user)
            # return HttpResponse('successful !')
            return render(request, 'user/login.html', {'msg': msg})
        msg = '用户名或密码错误!'
        return render(request, 'user/login.html', {'msg': msg})
        # return HttpResponse('fail !')
# 登出
def user_logout(request):
    # 清除session
    logout(request)
    return redirect('/task/')

# 主页面
def home(request):
    return render(request, 'user/home.html')


@login_required
def create(request):
    return HttpResponse('create')