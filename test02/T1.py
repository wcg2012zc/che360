#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/5 0005   17:02
# 文件     ：T1.py
# IDE      : PyCharm


import unittest
from init import InitTest


class BaiduTest(InitTest):
    def test_baidu_news(self):
        #验证：测试百度首页点击新闻的跳转
        self.driver.find_element_by_link_text("新闻").click()
        self.assertEquals(self.driver.current_url,'http://news.baidu.com/')

    def test_baidu_map(self):
        #验证：测试百度地图页面的跳转
        self.driver.find_element_by_link_text('地图').click()
        self.assertEquals(self.driver.current_url,'http://map.baidu.com/')

if __name__ == '__main__':
    unittest.main(verbosity=2)


