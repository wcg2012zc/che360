#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/8 0008   18:24
# 文件     ：Driver1.py
# IDE      : PyCharm

"""driver配置文件把浏览器初始化操作封装成一个类方便调用"""
from selenium import webdriver
import unittest


class DriverHandle(unittest.TestCase):#重命名这个类的名称，import这个类使用
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.360che.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

def tearDown(self):
    self.driver.quit()