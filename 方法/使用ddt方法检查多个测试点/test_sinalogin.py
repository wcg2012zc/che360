#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/7 0007   12:09
# 文件     ：test_sinalogin.py
# IDE      : PyCharm

from selenium import webdriver
import unittest
from ddt import data,unpack,ddt


@ddt
class sinaTest(unittest.TestCase):
    def setUp(self):#打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.get('https://mail.sina.com.cn/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):#关闭浏览器
        self.driver.quit()

    @data(('', '', '请输入邮箱名'), ('', 'admin', '请输入邮箱名'), ('admin', '', '您输入的邮箱名格式不正确'))
    #data中表示元组的列表数据

    @unpack#解压多个元组
    def test_Login(self, uersname, password, result):
        """验证：登录的N种情况"""
        self.driver.find_element_by_id('freename').send_keys(uersname)
        self.driver.find_element_by_id('freepassword').send_keys(password)
        self.driver.find_element_by_link_text('登录').click()
        divText = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
        self.assertEquals(divText, result)


if __name__ == '__main__':
    unittest.main(verbosity=2)


