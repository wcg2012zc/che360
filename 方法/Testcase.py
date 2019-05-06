#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/4/29 9:01
# 文件     ：Testcase.py
# IDE      : PyCharm

#unittest
from lib2to3.pgen2 import driver

from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.action_chains import ActionChains

class Che360Test(unittest.TestCase):
    @classmethod#装饰器，执行多用例，打开一次浏览器关闭一次
    def setUpClass(cls):
        print('进入网站')
        cls.dr = webdriver.Chrome()
        cls.dr.maximize_window()
        cls.dr.get('http://www.360che.com')#测试的地址
        cls.dr.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        print('结束测试')
        cls.dr.quit()

    def test_001(self):
        print('执行测试')#360che登录
        #悬停在登录按钮上
        ele = self.dr.find_element_by_xpath('//*[@id="sign"]/div[2]/a')
        #悬停在网友登录
        ActionChains(self.dr).move_to_element(ele).click()
        self.dr.find_element_by_xpath('//*[@id="sign"]/div[2]/a').click()
        self.dr.find_element_by_xpath('//*[@id="J_LoginUser"]').send_keys('13426230241')
        self.dr.find_element_by_xpath('//*[@id="J_LoginPsw"]').send_keys('360che')
        self.dr.find_element_by_xpath('//*[@id="J_LoginButton"]').click()
        sleep(5)

    def test_002(self):
        print('进入资讯')#浏览资讯页面
        self.dr.find_element_by_xpath('//*[@id="sitenav"]/dl[1]/dt/a').click()
        #先获取当前窗口的句柄
        handles = self.dr.window_handles
        #进行窗口切换，选择要切换的窗口
        self.dr.switch_to.window(handles[1])
        #拖动滚动条进行向下移动1000位置
        js = "var q=document.documentElement.scrollTop=500"
        self.dr.execute_script(js)
        sleep(3)
        #抢沙发进入评论页面
        self.dr.find_element_by_xpath('//*[@id="110291"]/div[2]/div[3]/div[2]/a').click()
        sleep(5)

    def test_003(self):
        handles = self.dr.window_handles
        # 进行窗口切换，选择要切换的窗口
        self.dr.switch_to.window(handles[0])
        print('进入产品库')#浏览产品库页面library
        self.dr.find_element_by_xpath('//*[@id="sitenav"]/dl[2]/dt/a').click()
        handles = self.dr.window_handles
        # 进行窗口切换，选择要切换的窗口
        self.dr.switch_to.window(handles[2])
        sleep(5)



"""
        #控制滚动条逐步滚动
        for y in range(15):
            js = "window.scrollBy(0,100)"
            webdriver.execute_script(js)
            sleep(1)
        #scrollTo(x,y) 中，x为必须参数，表示要在窗口文档显示区左上角显示的文档的x坐标；y也为必须参数，表示要在窗口文档显示区左上角显示的文档的y坐标
        webdriver.execute_script("window.scrollTo(0,1000)")
        #滑动---scrollBy(x,y)中，x为必须参数，表示向右滚动的像素值；y也为必须参数，
        #表示向下滚动的像素值
        webdriver.execute_script("window.scrollBy(0,1000)")
"""


if __name__ == '__main__':
    unittest.main(verbosity=2)

