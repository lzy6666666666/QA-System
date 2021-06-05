from Crawler.GetTime import getTime
from py2neo import Graph


class Query:
    # 初始化数据库
    def __init__(self):
        self.graph = Graph("http://localhost:7474", username="neo4j", password="lzy1022")

        # 查找数据库
    def run(self, cql):
        result = []
        find_rela = self.graph.run(cql)
        for i in find_rela:
            result.append(i.items()[0][1])
        return result

        # 查找类别判断
    def search(self, name, number):
        if name == 0:
            final_answer = " 输入问题有误，请重新输入!" \
                    "\n您可以输入以下有关电影的问题:" \
                    "\n例如:《龙兄虎弟》的评分/上映时间/简介/风格/演员/ 等等？" \
                    "\n（由于知识图谱数据有限，可能收录电影的范围有一定局限性）"
            # final_answer = " 输入问题有误，请重新输入!"
            return final_answer
        if name == 1:
            final_answer = " 确实是个傻逼！(￣▽￣)"
            return final_answer
        if name == 2:
            final_answer = "华师石牌校区四大天王之一，收到的情书比山还要高"
            return final_answer
        if name == 3:
            final_answer = "门岗: 石牌校区西门"\
                "\n学号: 20172131110"\
                "\n姓名: 李臻诣"\
                "\n单位: 计算机学院"\
                "\n电话: 13828207002"\
                "\n"\
                "\n【可通行】 请假获批，有效时段"\
                "\n"\
                "\n疫情防控关键时期，在校学生未经学校同意不得进出校园。"\
                "\n"\
                + getTime()
            return final_answer
        if name == 4:
            final_answer = "门岗: 石牌校区西门" \
                           "\n学号: 20172131003" \
                           "\n姓名: 潘峰" \
                           "\n单位: 计算机学院" \
                           "\n电话: 15626460102" \
                           "\n" \
                           "\n【可通行】 请假获批，有效时段" \
                           "\n" \
                           "\n疫情防控关键时期，在校学生未经学校同意不得进出校园。" \
                           "\n" \
                           + getTime()
            return final_answer
        if number == 0:
            cql = f"match (m:Movie)-[]->() where m.title='{name}' return m.rating"
            answer = self.run(cql)[0]
            answer = round(answer, 2)
            final_answer = name + "电影评分为" + str(answer) + "分！"
            return final_answer
        elif number == 1:
            cql = f"match(m:Movie)-[]->() where m.title='{name}' return m.releasedate"
            answer = self.run(cql)[0]
            final_answer = name + "的上映时间是" + str(answer) + "！"
            return final_answer
        elif number == 2:
            cql = f"match(m:Movie)-[r:is]->(b) where m.title='{name}' return b.name"
            answer = self.run(cql)
            answer_set = set(answer)
            answer_list = list(answer_set)
            answer = "、".join(answer_list)
            final_answer = name + "是" + str(answer) + "等类型的电影！"
            return final_answer
        elif number == 3:
            cql = f"match(m:Movie)-[]->() where m.title='{name}' return m.introduction"
            answer = self.run(cql)[0]
            final_answer = name + "主要讲述了" + str(answer) + "！"
            return final_answer
        elif number == 4:
            cql = f"match(n:Person)-[r:actedin]->(m:Movie) where m.title='{name}' return n.name"
            answer = self.run(cql)
            answer_set = set(answer)
            answer_list = list(answer_set)
            answer = "、".join(answer_list)
            final_answer = name + "由" + str(answer) + "等演员主演！"
            return final_answer
        elif number == 5:
            cql = f"match(n:Person)-[]->() where n.name='{name}' return n.biography"
            answer = self.run(cql)[0]
            final_answer = answer
            return final_answer
        elif number == 6:
            cql = f"match(n:Person)-[]->(m:Movie) where n.name='{name}' return m.title"
            answer = self.run(cql)
            answer_set = set(answer)
            answer_list = list(answer_set)
            answer = "、".join(answer_list)
            final_answer = name + "演过" + str(answer) + "等电影！"
            return final_answer
