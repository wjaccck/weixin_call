#coding=utf-8

from __future__ import unicode_literals

from django.db import models
from abstract.models import CommonModel
# Create your models here.
class Weixin_msg(CommonModel):
    action=models.CharField(max_length=10)
    agentid=models.CharField(max_length=100)
    fromuser=models.CharField(max_length=100)
    content=models.TextField()
    status=models.CharField(max_length=10)
    result=models.CharField(max_length=100,blank=True)

    @staticmethod
    def verbose():
        return u'微信信息'

class Action_list(CommonModel):
    name=models.CharField(max_length=25,unique=True)
    token=models.CharField(max_length=50)
    method=models.CharField(max_length=10)
    http_url=models.URLField()

    @staticmethod
    def verbose():
        return u'动作'