import random
def yanzhengma(num):
    list1 = 'dsadakmlfaskljfklsajklj1lk3jl2jkl5342j5kljkldsalk'
    code = ''
    for i in range(num):
        s1 = random.randint(0, len(list1) - 1)
        code = code + list1[s1]
    return code
result = yanzhengma(5)
print(result)