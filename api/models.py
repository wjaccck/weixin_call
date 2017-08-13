#coding=utf-8

from __future__ import unicode_literals

from django.db import models
from abstract.models import CommonModel
# Create your models here.
class Weixin_msg(CommonModel):
    action=models.CharField(max_length=10)
    project=models.CharField(max_length=50)
    args=models.CharField(max_length=100)
    agentid=models.CharField(max_length=100)
    fromuser=models.CharField(max_length=100)
    content=models.TextField()
    status=models.CharField(max_length=10)

    @staticmethod
    def verbose():
        return u'微信信息'