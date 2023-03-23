from decimal import Decimal

res = Decimal('10.10')
b = 10.10
print(res, type(res))
assert b == float(res)
