import hashlib
import time
from typing import Optional, Awaitable

import tornado as tornado

from wxreply import receive_msg, receive_event, reply_text
import xml.etree.ElementTree as ET
import tornado.ioloop
import tornado.web
# from tornado import httpserver


class wxStartHandler(tornado.web.RequestHandler):
    """
    微信服务器签名验证和消 息回复
    check_signature: 校验signature是否正确
    """

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    @staticmethod
    def check_signature(signature, timestamp, nonce):
        """校验token是否正确"""
        # 这个是token 和我们在微信公众平台配置接口填写一致
        token = 'lzy'
        L = [timestamp, nonce, token]
        L.sort()
        s = L[0] + L[1] + L[2]
        sha1 = hashlib.sha1(s.encode('utf-8')).hexdigest()
        # 对于验证结果返回true or false
        return sha1 == signature

    #
    def get(self):
        """这是get请求，处理配置接口验证的"""

        # 获取参数
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')
        echostr = self.get_argument('echostr')
        # 调用验证函数
        result = self.check_signature(signature, timestamp, nonce)
        if result:
            self.write(echostr)
        else:
            self.write('Not Open')

    def post(self):
        """ 这是post请求 接收消息，获取参数 """
        body = self.request.body
        # 返回的bodys是xml格式，通过ET转换为键值对格式，方便提取信息
        data = ET.fromstring(body)
        ToUserName = data.find('ToUserName').text
        FromUserName = data.find('FromUserName').text
        MsgType = data.find('MsgType').text
        # 如果发送的是消息请求，判断是文字还是语音，因为我们取发送的内容位置不一样
        if MsgType == 'text' or MsgType == 'voice':
            MsgId = data.find("MsgId").text
            if MsgType == 'text':
                Content = data.find('Content').text  # 文本消息内容
            elif MsgType == 'voice':
                Content = data.find('Recognition').text  # 语音识别结果，UTF8编码
            # 调用回复函数判断接受的信息，然后返回对应的内容
            reply_content = receive_msg(Content)
            CreateTime = int(time.time())
            # 调用回复信息封装函数，要指定用户，时间和回复内容
            out = reply_text(FromUserName, ToUserName, CreateTime, reply_content)
            self.write(out)

        # 如果接收的是事件，我们也要处理
        elif MsgType == 'event':
            Event = data.find('Event').text
            Event_key = data.find('EventKey').text
            CreateTime = int(time.time())
            # 判断事件，并返回内容
            reply_content = receive_event(Event, Event_key)
            if reply_content:
                out = reply_text(FromUserName, ToUserName, CreateTime, reply_content)
                self.write(out)


def main():
    application = tornado.web.Application([
        (r'/wx', wxStartHandler),  # 验证配置接口和消息回复路由
    ],
        autoreload=False,
        debug=False
    )
    # application.listen(9000) #http服务器开启
    # 下面代码是配置https服务器，当然选用http服务器也是可以的
    # server = httpserver.HTTPServer(application, ssl_options={
    #     "certfile": "server.crt",
    #     "keyfile": "server.key",
    # }
    #                                )
    application.listen(8000)  # 单进程开启
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
    # test