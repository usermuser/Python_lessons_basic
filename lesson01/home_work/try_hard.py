# -*- coding: utf-8 -*-
from math import sqrt

a = input('Please enter positive number a, =')
b = input('Please enter b =')
c = input('Please enter variable c =')

d = (b**2) - (4*a*c)
# y = a*x**2 + b*x + c
s = sqrt(b**2 - 4*a*c)
x1 = (-b+sqrt((b**2)-(4*a*c))/(2*a)

x2=(-b-s)/(2*a)

s = sqrt(b**2 - 4*a*c)

    if d > 0:
    print("d > 0, there is two real roots")
    print("x1 =", x1, "x2 =", x2)
elif d == 0:
    print("d == 0, there is two real roots and they are equal")
    print("x1 =", x1, "x2 =", x2)
elif d < 0:
    print("d < 0, there is two roots and they are complex")
    print("x1 =", x1, "x2 =", x2)
