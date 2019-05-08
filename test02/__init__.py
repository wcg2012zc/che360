#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/5 0005   16:52
# 文件     ：config.ini.py
# IDE      : PyCharm

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