#!usr/bin/env python
# -*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/4/30 0030   11:25
# 文件     ：Tsetsuite.py
# IDE      : PyCharm
import unittest


from 方法.Driver1 import Che360Test
from basepage import Basic


class che360test(Che360Test,Basic):
    def test_title01(Basic):
        #验证：浏览器的title
        Basic.ActionChains_class('more')
        Basic.clickelement_xpath('//*[@id="sitenav"]/dl[2]/dt/a')
        print('执行了吗')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule('unittest1.py')
    unittest.TextTestRunner(verbosity=2).run(suite)










