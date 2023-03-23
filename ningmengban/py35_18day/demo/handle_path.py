import os
# p1 = os.path.abspath('code.txt')
# print(p1)
# p2 = os.path.abspath('..')
# print(p2)
# p3 = os.path.abspath('.')
# print(p3)
# fp = __file__
# print(fp)

res = os.path.abspath(__file__)
dir_path = os.path.dirname(res)
base_path = os.path.dirname(dir_path)
print(base_path)