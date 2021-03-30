
"""处理客户发送信息的文件"""
from QA.nb_div import QuestionPrediction, getName
from QA.query import Query


def reply_text(FromUserName, ToUserName, CreateTime, Content):
    """回复文本消息模板"""
    textTpl = """<xml> <ToUserName><![CDATA[%s]]></ToUserName> <FromUserName>
    <![CDATA[%s]]></FromUserName> <CreateTime>%s</CreateTime> <MsgType><![CDATA[%s]]>
    </MsgType> <Content><![CDATA[%s]]></Content></xml>"""
    out = textTpl % (FromUserName, ToUserName, CreateTime, 'text', Content)
    return out


def receive_msg(msg):
    # 这是一个将疑问改成成熟句子的函数，例如：你好吗 公众号回复：你好
    # if msg[-1] == u'吗':
    #     return msg[:len(msg) - 1]
    # elif len(msg) > 2 and msg[-2] == u'吗':
    #     return msg[:len(msg) - 2]
    # else:
    #     return "你说的话我好像不明白？"

    name = getName(msg)  # 获取电影名字

    question_model = QuestionPrediction()  # 建立问题预测类
    query1 = Query()  # 建立索引类 匹配图数据库

    number = question_model.predict(msg)  # 获得电影的序号
    answer = query1.search(name, number)  # 获得QA回答
    return answer


def receive_event(event, key):
    # 如果是关注公众号事件
    if event == 'subscribe':
        reply = "感谢您关注本智能问答小公众号！" \
                "\n请输入所需询问有关电影的问题:" \
                "\n例如:《龙兄虎弟》的评分/上映时间/简介/风格/类型/演员是谁 等等？" \
                "\n"
        return reply
    # 如果是点击菜单拉取消息事件
    elif event == 'CLICK':
        # 接下来就是根据你点击不同的菜单拉去不同的消息啦
        # 我为了省事，不进行判断啦，如果需要判断请根据 key进行判断
        return "你点击了菜单" + key
    # 如果是点击菜单跳转Url事件，不做任何处理因为微信客户端会自行处理
    elif event == 'VIEW':
        return None