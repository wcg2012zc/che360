#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/5 0005   17:24
# 文件     ：init.py
# IDE      : PyCharm
"""driver配置文件"""
from selenium import webdriver
import unittest


class Che360Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.360che.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

def tearDown(self):
    self.driver.quit()