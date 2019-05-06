#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/4/30 0030   11:25
# 文件     ：Tsetsuite.py
# IDE      : PyCharm
from selenium import webdriver
import unittest

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()
        url = self.driver.current_url
        self.assertEquals(url,'http://news.baidu.com/')

    def test_baidu_map(self):
        self.driver.find_element_by_link_text('地图').click()
        self.driver.get('http://www.baidu.com')

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(BaiduTest('test_baidu_news'))
#     suite.addTest(BaiduTest("test_baidu_map"))
#     unittest.TextTestRunner(verbosity=2).run(suite)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BaiduTest)
    unittest.TextTestRunner(verbosity=2).run(suite)










