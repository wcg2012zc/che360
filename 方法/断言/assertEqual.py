#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/6 0006   8:30
# 文件     ：assertEqual.py
# IDE      : PyCharm

"""判断两个值是否相等"""
from selenium import webdriver
import unittest

class Che360Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_title(self):
        """验证：测试百度首页的title"""
        self.assertEquals(self.driver.title,'百度一下，你就知道')
if __name__ == '__main__':
    unittest.main(verbosity=2)
