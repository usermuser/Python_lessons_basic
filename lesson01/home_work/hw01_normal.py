# coding: utf-8
__author__ = 'Хусаинов Рустам Азатович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
user_input = input('Введите целое беззнаковое число, например 12345.\n\
Задача решена с помощью цикла while. ')

'''
This version of program i tried to solve using while operator
Checking that user input is correct not implemented since we assume that
user will enter correct type of number
'''

user_input_list = list(user_input)
input_length = len(user_input_list)
i=0
max = 0
while i < input_length:
    if int(user_input_list[i]) > int(max):
        max = user_input_list[i]
        i+=1
    else:
        i+=1
print('max digit in entered number is', max)


user_input = input('Введите целове баззнаковое число, например 23213.\n\
Задача решена с применением цикла for. ')
user_input_list = list(user_input)
input_length = len(user_input_list)
for i in range(input_length):
    if int(user_input_list[i]) > int(max):
        max = user_input_list[i]
        i+=1
    else:
        i+=1
print('Максимальное число из введенных цифр ', max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4.
