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
并确保之前无图数据 即graph.db文件，如果有删除再导入，导入前需在命令行输入neo4j service install
并且启动neo4j服务 start neo4j
登录http://localhost:7474/browser/
连接数据图设置好密码，在命令行导入csv_data里txt文档的语句
成功后链接Neo4j即可查看到构建完成的知识图谱

3.tornado搭建的服务器需要借助域名映射链接微信公众号平台，建议使用花生壳，
注册免费赠送域名网址。首先需在微信公众号平台创建个人微信订阅号，并进行微信签名认证，
若成功则表明本地服务器可以与微信服务器连通。此时运行tornado文件，即可在订阅号端使用项目。
