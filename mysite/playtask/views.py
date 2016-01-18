from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

from .models import Task
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#

def index(request):
    latest_task_list = Task.objects.order_by('-update')[:5]
    # template = loader.get_template('index_test.html')
    # output = ', '.join([q.title for q in latest_task_list])
    # print output
    # return HttpResponse(output)

    context = {"latest_task_list":latest_task_list}

    # return HttpResponse(template.render(context, request))
    return render(request, "index.html", context)



def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")