#coding=utf-8
from celery import Task as T
from core.common import logger,Send_message
from api.models import Weixin_msg
import time

class BaseTask(T):
    error_info = None
    logger = logger

    def init(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        pass

class MissionTask(BaseTask):
    error_info = None
    success_info = None
    exec_id, todo_mission = None, None
    mission = None

    def init(self, call_id,status,result):
        self.msg = Weixin_msg.objects.get(id=call_id)
        self.msg.status = status
        self.msg.result = result
        self.mission.save()
        super(MissionTask, self).init()

    def run(self,call_id,status,result):
        self.init(call_id,status,result)
        Send_message().run(self.msg.agentid,[self.msg.fromuser],result)