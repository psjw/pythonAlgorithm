import decimal

c=4.5
print(round(c))
context =decimal.getcontext()
context.rounding=decimal.ROUND_HALF_UP
print(round(decimal.Decimal(c)))

a = 4.500
print(round(a)) #정확히 4.5일 경우 짝수쪽으로 감
b = 4.501
print(round(b))

a=a+0.5
a=int(a)
print(a)

d=5.4
d+=0.5
print(int(d))

