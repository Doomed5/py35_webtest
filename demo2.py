import math
import random

a = random.randint(1, 10)
print(a)
if a > math.pi:

    s = math.pi*a*a
    print(s)
lst = []
i = 0
for i in range(100):
    n = random.randint(1, 10)
    lst.append(n)
    i += 1
print(lst)
