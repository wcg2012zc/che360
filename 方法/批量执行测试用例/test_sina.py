#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/6 0006   14:53
# 文件     ：test_sina.py
# IDE      : PyCharm

import unittest
from time import sleep

from selenium import webdriver

class sinaTest(unittest.TestCase):
    def setUp(self):#打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.get('https://mail.sina.com.cn/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):#关闭浏览器
        self.driver.quit()

    def test_username_password_null(self):
        #验证：新浪登录页面用户名和密码为空提示错误信息
        self.driver.find_element_by_id('freename').send_keys('')
        self.driver.find_element_by_id('freepassword').send_keys('')
        self.driver.find_element_by_link_text('登录').click()
        sleep(3)
        divError = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/'
           'div/div[4]/div[1]/div[1]/div[1]/span[1]').text#出现错误提示的判断
        self.assertEqual(divError,'请输入邮箱名')#判断是否弹出提示“请输入邮箱名”

if __name__ == '__main__':
    unittest.main(verbosity=2)


