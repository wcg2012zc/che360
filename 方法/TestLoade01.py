#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/5 0005   16:43
# 文件     ：TestLoade01.py
# IDE      : PyCharm

from selenium import webdriver
import unittest
"""加载测试类"""
class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_baidu_news(self):#验证：点击新闻页面后的跳转
        self.driver.find_element_by_link_text('新闻').click()
        self.assertEquals(self.driver.current_url, 'http://news.baidu.com/')

    def test_002(self):#验证：点击地图按钮后的跳转
        self.driver.find_element_by_link_text('地图').click()
        self.assertEquals(self.driver.current_url,'http://map.baidu.com/')


@staticmethod
def suite(testCaseClass):
    suite = unittest.TestLoader.loadTestsFromTestCase(testCaseClass)
    return suite

if __name__ == '__main__':
    suite = unittest.TextTestRunner(verbosity=2).run(BaiduTest.suite(BaiduTest))