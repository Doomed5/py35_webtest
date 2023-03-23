list1 = [213,'asd',222,'asd']
print(list1.index(222))
print(list1.count('asd'))
if 222 in list1:
    print('baohan')

list1.append("12312")
print(list1)
list1.extend('123adsa')
print(list1)
list1.extend([1,2,3])
print(list1)
list1.insert(1,143)
print(list1)
list1.pop()
print(list1)
list1.remove('a')
print(list1)
del list1[1]
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)