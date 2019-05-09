#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/9 0009   22:34
# 文件     ：singleton.py
# IDE      : PyCharm

def singleton(cls,*args,**kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return _singleton