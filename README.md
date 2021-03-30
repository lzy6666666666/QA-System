# QA-System
# 基于图数据库以及python有关电影的智能问答系统
图数据库本人采用的是流行的neo4j(neo4j-community-4.2.3)社区版
并结合jieba分词以及sklearn包对自然语言处理分类
本人则是采用注册的微信订阅号（公众号要钱）作为项目的前端
crawler文件为爬虫文件 爬取的是豆瓣电影的信息
QA文件主要为问答系统后台 主要为索引neo4j数据库以及nlp（自然语言处理）
QA.py可以运行于普通命令行，若结合微信公众号则需运行tornado_main.py


配置准备:
1.在官网下载neo4j社区版并根据相关教程配置环境
2.导入csv_data文件
具体方式为在neo4j目录找到import目录，并将csv_data数据复制到目录下
并确保之前
