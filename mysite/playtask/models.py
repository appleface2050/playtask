# coding=utf-8
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
from util.basemodel import JSONBaseModel

class Appetite(JSONBaseModel):
    """
    欲望表
    """
    status = models.BooleanField(default=True, db_index=True, verbose_name=u'是否启用')
    title = models.CharField(max_length=100, verbose_name=u'欲望名字')
    score = models.IntegerField(default=0, db_index=True, verbose_name=u'分值')
    # update = models.DateTimeField(default=datetime.datetime.now(), db_index=True, verbose_name=u'创建时间')
    update = models.DateTimeField(default=timezone.now, db_index=True, verbose_name=u'创建时间')


class AppetiteCompleted(JSONBaseModel):
    """
    完成欲望表
    """
    user_id = models.IntegerField(db_index=True, verbose_name=u'用户id')
    appetite_id = models.IntegerField(db_index=True, verbose_name=u'完成的欲望id')
    score = models.IntegerField(default=0, db_index=True, verbose_name=u'分值')
    # complete_time = models.DateTimeField(default=datetime.datetime.now(), db_index=True, verbose_name=u'完成时间')
    complete_time = models.DateTimeField(default=timezone.now, db_index=True, verbose_name=u'完成时间')

    @classmethod
    def add_appetite_record(cls,user_id,appetite_id,score):
        ac = AppetiteCompleted()
        ac.appetite_id = appetite_id
        ac.user_id = user_id
        ac.score = score
        ac.save()

class Task(JSONBaseModel):
    """
    任务表
    """
    status = models.BooleanField(default=True, db_index=True, verbose_name=u'是否启用')
    title = models.CharField(max_length=100, verbose_name=u'任务表')
    score = models.IntegerField(default=0, db_index=True, verbose_name=u'分值')
    type = models.IntegerField(default=0, db_index=True, verbose_name=u'任务类型 2普通任务 1每日任务 2每月任务')
    # update = models.DateTimeField(default=datetime.datetime.now(), db_index=True, verbose_name=u'创建时间')
    update = models.DateTimeField(default=timezone.now, db_index=True, verbose_name=u'创建时间')


class TaskCompleted(JSONBaseModel):
    """
    完成任务表
    """
    user_id = models.IntegerField(db_index=True, verbose_name=u'用户id')
    task_id = models.IntegerField(db_index=True, verbose_name=u'完成的任务id')
    score = models.IntegerField(default=0, db_index=True, verbose_name=u'分值')
    complete_time = models.DateTimeField(default=timezone.now, db_index=True, verbose_name=u'完成时间')

    @classmethod
    def add_task_record(cls,user_id,task_id,score):
        tc = TaskCompleted()
        tc.user_id = user_id
        tc.task_id = task_id
        tc.score = score
        tc.save()


class User(JSONBaseModel):
    """
    用户信息表，记录用户名，分数
    """
    user_name = models.CharField(max_length=50, db_index=True, verbose_name=u"用户名称")
    user_desc = models.CharField(null=True, max_length=200, verbose_name=u"描述")
    score = models.IntegerField(default=0, db_index=True, verbose_name=u'用户当前分数')
    status = models.BooleanField(default=True, db_index=True, verbose_name=u'是否启用')

    @classmethod
    def get_admin_score(cls):
        return User.objects.get(pk=1).score

    @classmethod
    def get_admin_user(cls):
        return User.objects.get(pk=1)

    @classmethod
    def add_score(cls,user_id,score):
        user = User.objects.get(pk=user_id)
        user.score += score
        user.save()

