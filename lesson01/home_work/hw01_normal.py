# -*- coding: utf-8 -*-
from math import sqrt

__author__ = 'Хусаинов Рустам Азатович'


# Задача-1: Дано произвольное целое число, вывести самую
# большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

user_input = input('Введите целое беззнаковое число, например 12345.\n\
Задача будет решена с помощью цикла while. ')
'''
This version of program i tried to solve using while operator
Checking that user input is correct not implemented since we assume that
user will enter correct type of number
'''

user_input_list = list(user_input)    # convert user input to list
input_length = len(user_input_list)   # get length of the list
i = 0
max = 0

while i < input_length:
    if int(user_input_list[i]) > int(max):
        max = user_input_list[i]
        i += 1
    else:
        i += 1
print('max digit in entered number is', max)


user_input = input('\nВведите целое баззнаковое число, например 23213.\n\
Задача решена с применением цикла for. ')
user_input_list = list(user_input)    # convert user input to list
input_length = len(user_input_list)   # get length of the list
max = 0

for i in range(input_length):               # compare all numbers in for cycle
    if int(user_input_list[i]) > int(max):  # if current number bigger than max
        max = user_input_list[i]            # max = current number
        i += 1
    else:
        i += 1
print('Максимальное число из введенных цифр ', max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = input('Please, enter first variable. a =')
b = input('Please, enter second variable. b =')
a, b = b, a
print("a = ", a, "b = ", b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4.

a = input('Please enter positive number a, =')
b = input('Please enter b =')
c = input('Please enter variable c =')

d = b**2 - 4*a*c
# y = a*x**2 + b*x + c
x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
if d > 0:
    print("d > 0, there is two real roots")
    print("x1 =", x1, "x2 =", x2)
elif d == 0:
    print("d == 0, there is two real roots and they are equal")
    print("x1 =", x1, "x2 =", x2)
elif d < 0:
    print("d < 0, there is two roots and they are complex")
    print("x1 =", x1, "x2 =", x2)
