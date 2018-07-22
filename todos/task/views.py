from django.shortcuts import render, redirect
from django.http import HttpResponse
from task.models import Task
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'task/home.html')

@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'task/create.html')
    elif request.method == 'POST':
        text = request.POST.get('title')
        task = Task(text=text, creator=request.user)
        task.save()
        return redirect(todo_list)

@login_required
def todo_list(request):
    user = request.user
    # 获取所有list
    # tasks = Task.objects.all()
    tasks = Task.objects.filter(creator=user.pk)
    return render(request, 'task/list.html', context={'todos':tasks})

def todo_update(request, pk):
    '''
    根据task的id更新task记录
    :param request:
    :return:
    '''
    # pk对应的task实例
    task = Task.objects.get(pk=pk)
    # 更新状态
    task.completed = not task.completed
    # 保存更改
    task.save()
    # 返回状态
    return redirect(todo_list)

def todo_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect(todo_list)
