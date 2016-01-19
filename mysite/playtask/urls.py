__author__ = 'appleface2050'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'^task_complete$', views.task_complete),
    url(r'^appetite_complete$', views.appetite_complete),

]