#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/5/6 0006   8:45
# 文件     ：assertFalse.py
# IDE      : PyCharm\
"""assertFalse和assertTrue，都是返回布尔类型的校验
    assertFalse要求返回的结果是False，才能执行成功
"""

import unittest
from init import InitTest1

class xinlang(InitTest1):
    def test_xinlang_mail(self):
        """验证：新浪邮箱登录页面取消自动登录"""
        isautoLogin = self.driver.find_element_by_id('store1')
        isautoLogin.click()
        self.assertFalse(isautoLogin.is_enabled())
if __name__ == '__main__':
    unittest.main(verbosity=2)
