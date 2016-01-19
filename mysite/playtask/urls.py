__author__ = 'appleface2050'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'^task_complete$', views.task_complete),
    url(r'^appetite_complete$', views.appetite_complete),
    url(r'^task_add$', views.task_add),
    url(r'^task_edit$', views.task_edit),
    url(r'^task_invalid$', views.task_invalid),
    url(r'^appetite_add$', views.appetite_add),
    url(r'^appetite_edit$', views.appetite_edit),
    url(r'^appetite_invalid$', views.appetite_invalid),

]