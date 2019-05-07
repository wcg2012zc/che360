#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/6 0006   8:39
# 文件     ：assertTrue.py
# IDE      : PyCharm
"""返回的是布尔类型"""
import unittest
from init import InitTest

class BaiduTest(InitTest):
    def test_baidu_news(self):
        so = self.driver.find_element_by_id('kw')
        self.assertTrue(so.is_enabled())

if __name__ == '__main__':
    unittest.main(verbosity=2)