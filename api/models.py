#coding=utf-8

from __future__ import unicode_literals

from django.db import models
from abstract.models import CommonModel
# Create your models here.
class Weixin_msg(CommonModel):
    action=models.CharField(max_length=10)
    project=models.CharField(max_length=50)
    args=models.CharField(max_length=100)
    content=models.TextField()

    @staticmethod
    def verbose():
        return u'项目信息'