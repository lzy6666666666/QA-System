from nb_div import QuestionPrediction, getName
from query import Query


def text_reply():
    print('请输入您所需询问有关电影的问题:')
    text = input()  # 输入问题
    # print(text)
    name = getName(text)  # 获取电影名字

    number = question_model.predict(text)
    answer = query1.search(name, number)
    print(answer)


if __name__ == '__main__':
    print("您好，欢迎使用电影问答系统")
    question_model = QuestionPrediction()
    query1 = Query()
    while 1:
        text_reply()