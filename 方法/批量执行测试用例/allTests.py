#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/6 0006   15:10
# 文件     ：allTests.py
# IDE      : PyCharm
import unittest
import os

def allCases():
    """获取所有测试模块"""
    suite = unittest.TestLoader().discover(
        #批量获取测试用例模块
        start_dir= os.path.dirname(__file__),
        #start_dir是测试模块的路径，存放在testCase包中
        pattern='test_*.py',
        #pattern用来获取testCase包中所有test开头的模块文件
        top_level_dir=None)
        #top_level_dir调用的时候直接给默认值None
    """discover方法代码：def discover(self,start_dir,pattern='test_*.py,top_level_dir=None):
    """
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(allCases())#执行所有测试模块


