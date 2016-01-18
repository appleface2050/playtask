# coding=utf-8
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Appetite(models.Model):
    """
    欲望表
    """
    status = models.BooleanField(default=True, db_index=True, verbose_name=u'是否启用')
    title = models.CharField(max_length=100, verbose_name=u'欲望名字')
    score = models.IntegerField(default=0, db_index=True, verbose_name=u'分值')
    # update = models.DateTimeField(default=datetime.datetime.now(), db_index=True, verbose_name=u'创建时间')
    update = models.DateTimeField(default=timezone.now, db_index=True, verbose_name=u'创建时间')

class AppetiteCompleted(models.Model):
    """
    完成欲望表
    """
    appetite_id = models.IntegerField(db_index=True, verbose_name=u'完成的欲望id')

    # score = models.IntegerField(default=0, db_index=True, verbose_name=u'分值')
    # complete_time = models.DateTimeField(default=datetime.datetime.now(), db_index=True, verbose_name=u'完成时间')
    complete_time = models.DateTimeField(default=timezone.now, db_index=True, verbose_name=u'完成时间')


class Task(models.Model):
    """
    任务表
    """
    status = models.BooleanField(default=True, db_index=True, verbose_name=u'是否启用')
    title = models.CharField(max_length=100, verbose_name=u'任务表')
    score = models.IntegerField(default=0, db_index=True, verbose_name=u'分值')
    type = models.IntegerField(default=0, db_index=True, verbose_name=u'任务类型 0每日任务 1每月任务 2普通任务')
    # update = models.DateTimeField(default=datetime.datetime.now(), db_index=True, verbose_name=u'创建时间')
    update = models.DateTimeField(default=timezone.now, db_index=True, verbose_name=u'创建时间')


class TaskCompleted(models.Model):
    """
    完成任务表
    """
    task_id = models.IntegerField(db_index=True, verbose_name=u'完成的任务id')
    # complete_time = models.DateTimeField(default=datetime.datetime.now(), db_index=True, verbose_name=u'完成时间')
    complete_time = models.DateTimeField(default=timezone.now, db_index=True, verbose_name=u'完成时间')




