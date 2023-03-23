filename = input('请输入要备份的文件名：')
index = filename.rfind('.')
name = filename[:index]
postfix = filename[index:]

newname = name + '备份'  +  postfix

old = open(filename,'rb')
new = open(newname,'wb')

while True:
    content = old.read(1024)
    if content == 0:
        break
    new.write(content)