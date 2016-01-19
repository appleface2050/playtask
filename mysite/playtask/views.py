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
        task_complate["task_title"] = Task.objects.get(pk=i.task_id).title
        task_complete_list.append(task_complate)
    for i in appetitecompleted_list:
        appetite = i.toJSON()
        appetite["appetite_title"] = Appetite.objects.get(pk=i.appetite_id).title
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

def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")


