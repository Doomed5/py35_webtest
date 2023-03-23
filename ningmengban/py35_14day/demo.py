import unittest

from py35_14day.register import register


class TestRegister(unittest.TestCase):
    def test_register(self):
        excepted = {'code': 1, 'mag': '注册成功'}
        data = ('python3', '123456', '123456')

        res = register(*data)
        self.assertEqual(excepted, res)

    def test_password_dis(self):
        excepted = {'code': 0, 'mag': '两次密码不一致'}
        data = ('python2', '123457', '123456')

        res = register(*data)
        self.assertEqual(excepted, res)

    def test_user_register(self):
        excepted = {'code': 0, 'mag': '账号已存在'}
        data = ('python31', '123456', '123456')

        res = register(*data)
        self.assertEqual(excepted, res)

    def test_password_gt18(self):
        excepted = {'code': 0, 'mag': '账号和密码长度必须在6-18位之间'}
        data = ('python4', '01234567899876543210', '01234567899876543210')

        res = register(*data)
        self.assertEqual(excepted, res)

    def test_password_lt6(self):
        excepted = {'code': 0, 'mag': '账号和密码长度必须在6-18位之间'}
        data = ('python5', '12345', '12345')

        res = register(*data)
        self.assertEqual(excepted, res)

    def test_user_gt18(self):
        excepted = {'code': 0, 'mag': '账号和密码长度必须在6-18位之间'}
        data = ('python61234567890123', '123456', '123456')

        res = register(*data)
        self.assertEqual(excepted, res)

    def test_user_lt6(self):
        excepted = {'code': 0, 'mag': '账号和密码长度必须在6-18位之间'}
        data = ('pytho', '123456', '123456')

        res = register(*data)
        self.assertEqual(excepted, res)
