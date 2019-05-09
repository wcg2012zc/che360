#!usr/bin/env python
# -*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/4/30 0030   11:25
# 文件     ：Tsetsuite.py
# IDE      : PyCharm
import unittest
from Util.Driver import DriverHandle
from Element.basepage import Basic,Assertions


class che360test(DriverHandle,Assertions):
    def test_title01(Assertions):
        #验证：浏览器的title
        Assertions.assertEqual_xpath('咨询','//*[@id="sitenav"]/dl[1]/dt/a')
        Assertions.assertEqual_xpath('直播','//*[@id="sitenav"]/dl[1]/dd/span[2]/a')
        print('执行了吗')


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2)










