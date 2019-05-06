#!usr/bin/env python
# -*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/4/30 0030   11:25
# 文件     ：Tsetsuite.py
# IDE      : PyCharm
from selenium import webdriver
import unittest
"""按测试模块执行"""

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_title(self):
        #验证：浏览器的title
        self.assertEquals(self.driver.title,'百度一下，你就知道')
    def test_so(self):
        #验证：输入框可编辑性:
        so = self.driver.find_element_by_id('kw')
        self.assertTrue(so.is_enabled())

    def test_001(self):#验证：点击新闻页面
        self.driver.find_element_by_link_text('新闻').click()
        url = self.driver.current_url
        self.assertEquals(url, 'http://news.baidu.com/')

    def test_002(self):#验证：点击地图按钮
        self.driver.find_element_by_link_text('地图').click()
        self.driver.get('http://www.baidu.com/')

    def tearDown(self):
        self.driver.quit()

class che360(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com/')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_360che_zixun(self):#点击资讯后跳转
        self.driver.find_element_by_link_text('地图').click()
        self.driver.get('http://www.baidu.com/')



# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(BaiduTest('test_baidu_news'))
#     suite.addTest(BaiduTest("test_baidu_map"))
#     unittest.TextTestRunner(verbosity=2).run(suite)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule('unittest1.py')
    unittest.TextTestRunner(verbosity=2).run(suite)










