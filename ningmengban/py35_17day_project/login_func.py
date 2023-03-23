"""
============================
Author:柠檬班-木森
Time:2020/12/1  20:14
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

users = [{'user': 'python31', 'password': '123456'}]


def register(username, password1, password2):
    # 判断是否有参数为空
    if not all([username, password1, password2]):
        return {"code": 0, "msg": "所有参数不能为空"}
    # 注册功能
    for user in users:  # 遍历出所有账号，判断账号是否存在
        if username == user['user']:
            # 账号存在
            return {"code": 0, "msg": "该账户已存在"}
    else:
        if password1 != password2:
            # 两次密码不一致
            return {"code": 0, "msg": "两次密码不一致"}
        else:
            # 账号不存在 密码不重复，判断账号密码长度是否在 6-18位之间
            if 6 <= len(username) >= 6 and 6 <= len(password1) <= 18:
                # 注册账号
                users.append({'user': username, 'password': password2})
                return {"code": 1, "msg": "注册成功"}
            else:
                # 账号密码长度不对，注册失败
                return {"code": 0, "msg": "账号和密码必须在6-18位之间"}


def login_check(username=None, password=None):
    """
    登录校验的函数
    :param username: 账号
    :param password:  密码
    :return: dict type
    """
    if username != None and password != None:
        if username == 'python35' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "所有的参数不能为空"}


if __name__ == '__main__':
    # 1、账号密码正确
    res = login_check('python35', 'lemonban')
    expected = {"code": 0, "msg": "登录成功"}
    # if res == expected:
    #     print("用例：正确的账号密码 --执行通过")
    assert res == expected
    # 2、密码错误
    res = login_check('python35', 'lemonban222')
    expected = {"code": 1, "msg": "账号或密码不正确"}
    assert res == expected
    # if res == expected:
    #     print("用例：密码错误 --执行通过")
