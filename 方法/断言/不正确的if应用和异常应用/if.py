#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/6 0006   9:04
# 文件     ：if.py
# IDE      : PyCharm
"""不正确的if使用，不管复选框是不是自动选中，判断的结果都是pass，严禁使用if else进行断言判定"""
import unittest
#from selenium import webdriver
from init import InitTest1
# class BaiduTest(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get('https://mail.sina.com.cn/')
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)

class test_sina_login(InitTest1):
    def test_xinlang_login(self):
        isAutoLogin = self.driver.find_element_by_id('store1')
        if isAutoLogin.is_selected():
            print('succcess')
        else:
            print('fail')

if __name__ == '__main__':
    unittest.main(verbosity=2)