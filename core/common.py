__author__ = 'jinhongjun'
import logging
logger = logging.getLogger("webapp")
import requests
from django.conf import settings
import json,httplib
def get_result(status,content):
    if status==0:
        result={
                "retcode":0,
                "stdout":content,
                "stderr":''
                }
    else:
        result={
                "retcode":status,
                "stdout":'',
                "stderr":content
                }
    return result
class Rest_api:
    def __init__(self):
        self.header = {"Authorization": "Token {0}".format(settings.PUBLISH_TOKEN), "Content-Type": "application/x-www-form-urlencoded"}
    def get(self, path):
        result=requests.get(path,headers=self.header)
        return result.status_code,result.content
    def post(self,path,data):
        result=requests.post(path,data=data,headers=self.header)
        return result.status_code,result.content

class Send_message(object):
    def __init__(self):
        self.header = {"Content-Type": "application/json"}
        self.host = 'qyapi.weixin.qq.com'
        self._get_token()
        # https://oapi.dingtalk.com/gettoken?corpid=id&corpsecret=secrect

    def _get_token(self):
        headers = {"Content-Type": "application/xml"}
        conn = httplib.HTTPSConnection(self.host, 443)
        conn.connect()
        conn.request('GET',
                     '/cgi-bin/gettoken?corpid=wx5d299f9a3fba1d89&corpsecret=TZOFryL5qR8SnBlwKszOdrMnCxR6dDZH1NAX-mvtXfwawuCAPwoUuOu0w2rz8MRd',
                     '', headers)
        result = conn.getresponse().read()
        self.token = json.loads(result).get('access_token')

    def _send_msg(self,agent_id,to_user, msg):
        headers = {"Content-Type": "application/xml"}
        conn = httplib.HTTPSConnection(self.host, 443)
        conn.connect()
        data = {
            "touser": "|".join(to_user),
            "msgtype": "text",
            "agentid": agent_id,
            "text": {
                "content": msg
            },
            "safe": 0
        }
        content = json.dumps(data)
        conn.request('POST', '/cgi-bin/message/send?access_token=%s' % self.token, content, headers)
        result = conn.getresponse().read()
        conn.close()
        return json.loads(result)

    def run(self, agent_id,to_user,msg):
        result= self._send_msg(int(agent_id),to_user,msg)
        return result