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

    @classmethod
    def add_appetite(cls,appetite_title,appetite_score):
        if int(appetite_score) > 0:
            appetite_score = -int(appetite_score)
        else:
            int(appetite_score)
        a = cls()
        a.score = appetite_score
        a.title = appetite_title
        a.save()

    @classmethod
    def edit_appetite(cls,appetite_id,appetite_title,appetite_score,appetite_status):
        if int(appetite_score) > 0:
            appetite_score = -int(appetite_score)
        else:
            int(appetite_score)
        a = cls.objects.get(pk=int(appetite_id))
        a.title = appetite_title
        a.score = appetite_score
        a.status = appetite_status

    @classmethod
    def invalid_appetite(cls,appetite_id):
        appetite_id = int(appetite_id)
        a = cls.objects.get(pk=appetite_id)
        a.status = False
        a.save()

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

    @classmethod
    def add_task(cls,task_title,task_score,task_type):
        t = cls()
        t.title = task_title
        t.score = int(task_score)
        t.type = int(task_type)
        t.save()

    @classmethod
    def edit_task(cls, task_id,task_title,task_score,task_type,task_status):
        t = cls.objects.get(pk=task_id)
        t.title = task_title
        t.status = task_status
        t.score = int(task_score)
        t.type = int(task_type)
        t.save()

    @classmethod
    def invalid_task(cls, task_id):
        task_id = int(task_id)
        t = cls.objects.get(pk=task_id)
        t.status = False
        t.save()

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

