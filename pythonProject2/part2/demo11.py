# def f(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#       return  f(n-1) + f(n-2)
# result = f(15)
# print(result)

# def f(n):
#     if n <= 2:
#         return  n
#
#     return n * f(n-1)
# result1 = f(4)
# print(result1)

def f(n):
    if n == 10:
        return 1
    return (f(n+1)+1)*2
print(f(1))
