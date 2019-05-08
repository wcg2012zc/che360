#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/7 0007   9:06
# 文件     ：AllTest.py
# IDE      : PyCharm

import unittest
import os
import HTMLTestRunner
import time

def allTests():
    """获取所有测试模块."""
    suite = unittest.TestLoader().discover(
        #批量获取测试用例模块
        start_dir= os.path.dirname(__file__),
        #start_dir是测试模块的路径，存放在testCase包中
        pattern='Test*.py',
        #pattern用来获取testCase包中所有test开头的模块文件
        top_level_dir=None)
        #top_level_dir调用的时候直接给默认值None
    """
    discover方法：def discover(self,start_dir,pattern='test_*.py,top_level_dir=None):
    """
    return suite

def getNowTime():
    """获取当前的时间"""
    return time.strftime('%Y-%M-%d %H_%M_%S',time.localtime(time.time()))

 #run方法用来执行执行测试套件中的测试用例和生成测试报告
def run():
    fileName = os.path.join(os.path.dirname(__file__), 'report', getNowTime()+'report.html')
    fp = open(fileName, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='UI 自动化测试报告',
        description='UI 自动化测试报告详细信息')
    runner.run(allTests())

if __name__ == '__main__':
    run()