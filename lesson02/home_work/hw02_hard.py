# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

print('Задача-1.')
equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
# y = -12*x+11111140.2121
split1=(equation.split('+'))
b = float(split1[1])
k = split1[0]
print(k)
print(b)
# s = "".join(l)  # convert back to string

newk = k.replace('y', '')
print(newk)

newk = newk.replace('=', '')
print(newk)

newk = newk.replace('x', '')
print(int(newk))


#
# list_k = list(k)
# print(list_k)
#
# str_k = str(k)
# print(str_k)

# if 'y' in k:
#     print(k.index('y'))
#
# if '=' in k:
#     print(k.index('='))

# list_k = list(k)

# if 'y' in k:
#     i = list_k.index('y')
#     list_k.pop(i)
#
# if '=' in k:
#     i = list_k.index('=')
#     list_k.pop(i)
#
# if 'x' in k:
#     i = list_k.index('x')
#     list_k.pop(i)
#
# #try to pop all whitespaces
# for i in list_k:
#     if i == ' ':
#         s = list_k.index(i)
#         list_k.pop(s)
# print(list_k)



# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3