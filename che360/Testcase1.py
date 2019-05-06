#!usr/bin/env python
# -*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/4/30 0030   11:25
# 文件     ：Tsetsuite.py
# IDE      : PyCharm
#from selenium import webdriver

import unittest

from Driver import Che360Test

class che360test(Che360Test):

    def test_title(self):
        #验证：浏览器的title
        self.assertEquals(self.driver.title,'卡车之家_商用车互动服务平台')
    def test_so(self):
        #验证：输入框可编辑性:
        so = self.driver.find_element_by_id('keyword')
        self.assertTrue(so.is_enabled())

    def test_001(self):#验证：点击资讯按钮
        self.driver.find_element_by_link_text('资讯').click()
        url = self.driver.current_url
        self.assertEquals(url, 'http://www.360che.com/')

    def test_002(self):#验证：点击报价库按钮
        self.driver.find_element_by_link_text('报价库').click()
        self.driver.get('http://www.360che.com/')

    def test_360che_zixun(self):#点击资讯后跳转
        self.driver.find_element_by_link_text('资讯').click()
        self.driver.get('http://www.360che.com/')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule('unittest1.py')
    unittest.TextTestRunner(verbosity=2).run(suite)










