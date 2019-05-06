#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/5   9:42
# 文件     ：Hello，world.py
# IDE      : PyCharm


from flask import Flask

app = Flask(__name__)  # 创建1个Flask实例


@app.route('/')  # 路由系统生成 视图对应url,1. decorator=app.route() 2. decorator(first_flask)
def first_flask():  # 视图函数
    return 'Hello World'  # response


if __name__ == '__main__':
    app.run()  # 启动socket