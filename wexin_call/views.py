# coding=utf8
from django.http import HttpResponse,HttpResponseBadRequest
from core.common import logger,Send_message
from core.WXBizMsgCrypt  import WXBizMsgCrypt
import xml.etree.cElementTree as ET
# from api.models import Weixin_msg
from django.conf import settings


def weixin_index(req):
    sToken = "Cm2ViWqz4nM2C4k4T8x"
    sEncodingAESKey = "r5n2sSsdEBG70Gb6GZFLB5lsZfspmuXW8eYs6Fk94S5"
    sCorpID = "wx5d299f9a3fba1d89"
    wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)
    if req.method == 'GET':
        logger.info('get request')
        logger.info(req.body)
        sVerifyMsgSig=req.GET.get('msg_signature')
        sVerifyTimeStamp=req.GET.get('timestamp')
        sVerifyNonce=req.GET.get('nonce')
        sVerifyEchoStr=req.GET.get('echostr')
        ret, sEchoStr = wxcpt.VerifyURL(sVerifyMsgSig, sVerifyTimeStamp, sVerifyNonce, sVerifyEchoStr)
        response=HttpResponse(sEchoStr)
        if (ret != 0):
            response = HttpResponseBadRequest('wrong')
        return response
    elif req.method =='POST':
        logger.info('post request')
        logger.info(req.body)
        sReqMsgSig=req.GET.get('msg_signature')
        sReqTimeStamp=req.GET.get('timestamp')
        sReqNonce=req.GET.get('nonce')
        sReqData=req.body
        # sReqData = "<xml><ToUserName><![CDATA[ww1436e0e65a779aee]]></ToUserName>\n<Encrypt><![CDATA[Kl7kjoSf6DMD1zh7rtrHjFaDapSCkaOnwu3bqLc5tAybhhMl9pFeK8NslNPVdMwmBQTNoW4mY7AIjeLvEl3NyeTkAgGzBhzTtRLNshw2AEew+kkYcD+Fq72Kt00fT0WnN87hGrW8SqGc+NcT3mu87Ha3dz1pSDi6GaUA6A0sqfde0VJPQbZ9U+3JWcoD4Z5jaU0y9GSh010wsHF8KZD24YhmZH4ch4Ka7ilEbjbfvhKkNL65HHL0J6EYJIZUC2pFrdkJ7MhmEbU2qARR4iQHE7wy24qy0cRX3Mfp6iELcDNfSsPGjUQVDGxQDCWjayJOpcwocugux082f49HKYg84EpHSGXAyh+/oxwaWbvL6aSDPOYuPDGOCI8jmnKiypE+]]></Encrypt>\n<AgentID><![CDATA[1000002]]></AgentID>\n</xml>"
        logger.info(sReqMsgSig)
        logger.info(sReqTimeStamp)
        logger.info(sReqNonce)
        logger.info(sReqData)
        logger.info(req.POST)

        ret, sMsg = wxcpt.DecryptMsg(sReqData, sReqMsgSig, sReqTimeStamp, sReqNonce)
        if (ret != 0):
            response = HttpResponseBadRequest('wrong')
        else:
            xml_tree = ET.fromstring(sMsg)
            content = xml_tree.find("Content").text
            AgentID = xml_tree.find("AgentID").text
            FromUserName = xml_tree.find("FromUserName").text
            info_line=content.split()
            # if info_line[0] in settings.ALLOWED_ACTION:

            logger.info(content)
            logger.info(AgentID)
            logger.info(FromUserName)
            Send_message().run(AgentID,[FromUserName],'Mission accept ! {0} will {1}'.format(info_line[1],info_line[0]))
            response = HttpResponse(content)
        return response



def weixin_index(req):
    sToken = "Cm2ViWqz4nM2C4k4T8x"
    sEncodingAESKey = "r5n2sSsdEBG70Gb6GZFLB5lsZfspmuXW8eYs6Fk94S5"
    sCorpID = "wx5d299f9a3fba1d89"
    wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)
    if req.method == 'GET':
        logger.info('get request')
        logger.info(req.body)
        sVerifyMsgSig=req.GET.get('msg_signature')
        sVerifyTimeStamp=req.GET.get('timestamp')
        sVerifyNonce=req.GET.get('nonce')
        sVerifyEchoStr=req.GET.get('echostr')
        ret, sEchoStr = wxcpt.VerifyURL(sVerifyMsgSig, sVerifyTimeStamp, sVerifyNonce, sVerifyEchoStr)
        response=HttpResponse(sEchoStr)
        if (ret != 0):
            response = HttpResponseBadRequest('wrong')
        return response
    elif req.method =='POST':
        logger.info('post request')
        logger.info(req.body)
        sReqMsgSig=req.GET.get('msg_signature')
        sReqTimeStamp=req.GET.get('timestamp')
        sReqNonce=req.GET.get('nonce')
        sReqData=req.body
        # sReqData = "<xml><ToUserName><![CDATA[ww1436e0e65a779aee]]></ToUserName>\n<Encrypt><![CDATA[Kl7kjoSf6DMD1zh7rtrHjFaDapSCkaOnwu3bqLc5tAybhhMl9pFeK8NslNPVdMwmBQTNoW4mY7AIjeLvEl3NyeTkAgGzBhzTtRLNshw2AEew+kkYcD+Fq72Kt00fT0WnN87hGrW8SqGc+NcT3mu87Ha3dz1pSDi6GaUA6A0sqfde0VJPQbZ9U+3JWcoD4Z5jaU0y9GSh010wsHF8KZD24YhmZH4ch4Ka7ilEbjbfvhKkNL65HHL0J6EYJIZUC2pFrdkJ7MhmEbU2qARR4iQHE7wy24qy0cRX3Mfp6iELcDNfSsPGjUQVDGxQDCWjayJOpcwocugux082f49HKYg84EpHSGXAyh+/oxwaWbvL6aSDPOYuPDGOCI8jmnKiypE+]]></Encrypt>\n<AgentID><![CDATA[1000002]]></AgentID>\n</xml>"
        logger.info(sReqMsgSig)
        logger.info(sReqTimeStamp)
        logger.info(sReqNonce)
        logger.info(sReqData)
        logger.info(req.POST)

        ret, sMsg = wxcpt.DecryptMsg(sReqData, sReqMsgSig, sReqTimeStamp, sReqNonce)
        if (ret != 0):
            response = HttpResponseBadRequest('wrong')
        else:
            xml_tree = ET.fromstring(sMsg)
            content = xml_tree.find("Content").text
            AgentID = xml_tree.find("AgentID").text
            FromUserName = xml_tree.find("FromUserName").text
            info_line=content.split()
            # if info_line[0] in settings.ALLOWED_ACTION:

            logger.info(content)
            logger.info(AgentID)
            logger.info(FromUserName)
            Send_message().run(AgentID,[FromUserName],'Mission accept ! {0} will {1}'.format(info_line[1],info_line[0]))
            response = HttpResponse(content)
        return response
