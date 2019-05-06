#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/5 0005   16:52
# 文件     ：init.py
# IDE      : PyCharm

"""将webdriver封装为一个方法进行调用"""
import unittest
from selenium import webdriver


class InitTest(unittest.TestCase):
    def setUp(self):#打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):#关闭浏览器
        self.driver.quit()

class InitTest1(unittest.TestCase):
    def setUp(self):#打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.get('https://mail.sina.com.cn/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):#关闭浏览器
        self.driver.quit()
