users = [{'user': 'python31', 'password': '123456'}]


def register(username, password1, password2):
    if username and password1 and password2 == False:
        return {'code': 0, 'mag': '所有参数不能为空'}
    for user in users:
        if username == user['user']:
            return {'code': 0, 'mag': '账号已存在'}
    else:
        if password1 != password2:
            return {'code': 0, 'mag': '两次密码不一致'}
        else:
            if 6 <= len(username) <= 18 and 6 <= len(password1) <= 18:
                users.append({"user": username, 'password': password2})
                return {'code': 1, 'mag': '注册成功'}
            else:
                return {'code': 0, 'mag': '账号和密码长度必须在6-18位之间'}


if __name__ == '__main__':
    res = register('python14', '123456', '123456')
    print(res)
