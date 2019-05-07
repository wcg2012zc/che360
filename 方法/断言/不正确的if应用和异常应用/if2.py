#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/6 0006   11:18
# 文件     ：if2.py
# IDE      : PyCharm
"""此代码与if结果一样，即使自动登录不被勾选，测试结果让是pass"""
import unittest

from init import InitTest1

class test_sina_login(InitTest1):
    def test_xinlang_login(self):
        isAutoLogin = self.driver.find_element_by_id('store1')
        try:
            self.assertTrue(isAutoLogin.is_selected())#判断复选框是不是自动化勾选
        except:
            print ('fail')

if __name__ == '__main__':
    unittest.main(verbosity=2)


