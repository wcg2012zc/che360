#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/5 0005   16:26
# 文件     ：__init__.py.py
# IDE      : PyCharm


import unittest
from selenium import webdriver


class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)


    def tearDown(self):
        self.driver.quit()