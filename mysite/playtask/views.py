# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.

from .models import Task,User,TaskCompleted,AppetiteCompleted,Appetite
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#

def index(request):
    """
    首页
    """
    current_user = User.get_admin_user()
    latest_task_list = Task.objects.filter(status=True).order_by('pk')
    appetite_list = Appetite.objects.filter(status=True).order_by('pk')
    taskcomplate_list = TaskCompleted.objects.filter(user_id=current_user.pk).order_by("-complete_time")[:5]
    appetitecompleted_list = AppetiteCompleted.objects.filter(user_id=current_user.pk).order_by("-complete_time")[:5]
    task_complete_list = []
    appetite_complete_list = []

    for i in taskcomplate_list:
        task_complate = i.toJSON()
        if Task.objects.filter(pk=i.task_id):
            task_complate["task_title"] = Task.objects.get(pk=i.task_id).title
        else:
            task_complate["task_title"] = "已删除"
        task_complete_list.append(task_complate)
    for i in appetitecompleted_list:
        appetite = i.toJSON()
        if Appetite.objects.filter(pk=i.appetite_id):
            appetite["appetite_title"] = Appetite.objects.get(pk=i.appetite_id).title
        else:
            appetite["appetite_title"] = "已删除"
        appetite_complete_list.append(appetite)

    context = {"latest_task_list":latest_task_list,
               "appetite_list":appetite_list,
               "taskcomplate_list":task_complete_list,
               "appetitecompleted_list":appetite_complete_list,
               "current_user":current_user}

    # return HttpResponse(template.render(context, request))
    return render(request, "index.html", context)


def task_complete(request):
    """
    完成任务
    """
    task_id = request.POST.get("task_id")
    # user_id = request.REQUEST.get("user_id")
    user_id = 1
    task = Task.objects.get(pk=task_id)
    User.add_score(user_id=user_id,score=task.score)
    TaskCompleted.add_task_record(user_id=user_id,task_id=task.pk,score=task.score)
    return HttpResponseRedirect('/playtask/')


def appetite_complete(request):
    """
    实现欲望
    """
    appetite_id = request.POST.get("appetite_id")
    user_id = 1
    appetite = Appetite.objects.get(pk=appetite_id)
    User.add_score(user_id=user_id,score=appetite.score)
    AppetiteCompleted.add_appetite_record(user_id=user_id,appetite_id=appetite.pk,score=appetite.score)
    return HttpResponseRedirect('/playtask/')


def appetite_add(request):
    """
    欲望增加
    """
    appetite_title = request.POST.get("appetite_title")
    appetite_score = request.POST.get("appetite_score")
    if appetite_title == u"" or appetite_score == u"":
        return HttpResponse("fail")
    try:
        Appetite.add_appetite(appetite_title,appetite_score)
    except:
        return HttpResponse("appetite add fail")
    else:
        return HttpResponseRedirect('/playtask/')

def appetite_edit(request):
    """
    欲望修改
    """
    appetite_id = request.POST.get("appetite_id")
    appetite_title = request.POST.get("appetite_title")
    appetite_score = request.POST.get("appetite_score")
    appetite_status = request.POST.get("appetite_status")
    if appetite_id == u"" or appetite_title == u"" or appetite_score == u"" or appetite_status == u"":
        return HttpResponse("fail")
    if appetite_status == u"0":
        appetite_status = False
    try:
        Appetite.edit_appetite(appetite_id,appetite_title,appetite_score,appetite_status)
    except:
        return HttpResponse("Appetite edit fail")
    else:
        return HttpResponseRedirect('/playtask/')

def appetite_invalid(request):
    """
    欲望隐藏
    """
    appetite_id = request.POST.get("appetite_id")
    if appetite_id == u"":
        return HttpResponse("fail")
    try:
        Appetite.invalid_appetite(appetite_id)
    except:
        return HttpResponse("Appetite invalid fail")
    else:
        return HttpResponseRedirect('/playtask/')


def task_add(request):
    """
    任务管理增加任务
    """
    task_title = request.POST.get("task_title")
    task_score = request.POST.get("task_score")
    task_type = request.POST.get("task_type")
    if not task_type:
        task_type = 0
    if task_title == u"" or task_score == u"":
        return HttpResponse("fail")
    try:
        Task.add_task(task_title,task_score,task_type)
    except:
        return HttpResponse("task add fail")
    else:
        return HttpResponseRedirect('/playtask/')

def task_edit(request):
    """
    任务管理修改任务
    """
    task_id = request.POST.get("task_id")
    task_title = request.POST.get("task_title")
    task_score = request.POST.get("task_score")
    task_type = request.POST.get("task_type")
    task_status = request.POST.get("task_status")
    if task_title == u"" or task_score == u"" or task_id == u"" or task_type == u"" or task_status == u"":
        return HttpResponse("fail")
    if task_status == u"0":
        task_status = False
    try:
        Task.edit_task(task_id,task_title,task_score,task_type,task_status)
    except:
        return HttpResponse("task edit fail")
    else:
        return HttpResponseRedirect('/playtask/')

def task_invalid(request):
    task_id = request.POST.get("task_id")
    if task_id == u"":
        return HttpResponse("fail")
    try:
        Task.invalid_task(task_id)
    except:
        return HttpResponse("task invalid fail")
    else:
        return HttpResponseRedirect('/playtask/')

def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def all_task(request):
    """
    获取所有task
    """
    data = Task.objects.all()
    return HttpResponse(data)