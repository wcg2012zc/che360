#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/6 0006   8:55
# 文件     ：assertln.py
# IDE      : PyCharm
"""assertIn指一个值是否包含另外一个值的范围"""
import unittest
from init import InitTest

class BaiduTest(InitTest):
    def test_baidu_news(self):
        """验证：百度首页是否一致"""
        self.assertIn(self.driver.current_url,'https://www.baidu.com/')

if __name__ == '__main__':
    unittest.main(verbosity=2)
