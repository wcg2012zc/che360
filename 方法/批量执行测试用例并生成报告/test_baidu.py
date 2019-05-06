#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/6 0006   14:52
# 文件     ：test_baidu.py
# IDE      : PyCharm

import unittest
from selenium import webdriver
from time import sleep


class InitTest(unittest.TestCase):#把所有的浏览器初始化封装为一个类进行调用
    def setUp(self):#打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_title(self):
        #验证：浏览器的title
        self.assertEquals(self.driver.title,'百度一下，你就知道')
        sleep(3)
if __name__ == '__main__':
    unittest.main(verbosity=2)

