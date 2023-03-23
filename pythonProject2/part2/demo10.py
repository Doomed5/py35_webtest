def menu():
    print('-'*20)
    print("    学生管理系统V1.0    ")
    print("1.添加学生的信息")
    print("2.删除学生的信息")
    print("3.修改学生的信息")
    print("4.查询学生的信息")
    print("5.遍历学生的信息")
    print("6.退出系统")
    print('-'*20)
students = []
def tianjia():
    students_dict = {}
    students_dict['name'] = input('输入学生的姓名：')
    students_dict['age'] = input('输入学的的年龄：')
    students_dict['phone'] = input('输入学生的电话：')
    global students
    students.append(students_dict)
    print('学员信息添加成功')

def shanchu():
    global students
    name = input('输入学生的姓名：')
    for i in students:
        if i['name'] == name:
            students.remove(i)
            print('删除成功')
            break
    else:
        print('未找到学员信息')

def xiugai():
    name = input('输入要修改的学生姓名：')
    global students
    for i in students:
        if i['name'] == name:
            i['name'] = input('输入修改后的姓名')
            i['age'] = input('输入修改后的年龄')
            i['phone'] = input('输入修改后的电话')
            print('修改成功')
            break
    else:
        print('未找到学员信息')
def chaxun():
    name = input('输入要查询的学生姓名：')
    for i in students:
        if i['name'] == name:
            print(f'姓名：{i["name"]}，年龄：{i["age"]}，电话：{i["phone"]}')
            break
    else:
        print('未查询到')
def bianli():
    for i in students:
        print(f'姓名：{i["name"]}，年龄：{i["age"]}，电话：{i["phone"]}')
# def tuichu():
#     print('欢迎使用')


menu()
while True:
    num = int(input("输入要操作的序号："))
    if num == 1:
        tianjia()
    elif num == 2:
        shanchu()
    elif num == 3:
        xiugai()
    elif num == 4:
        chaxun()
    elif num == 5:
        bianli()
    elif num == 6:
        print('欢迎使用')
        break
    else:
        print("输入错误")
print(students)