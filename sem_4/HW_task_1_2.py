# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
d= float(input())
d=len(str(d))
print(str(pi)[:d])


# print('\nTask1')
#
# import math
#
# print(math.pi)
#
#
# def pi_accuracy(acc, ln):
#     den = 3
#     pi_acc = 4
#     tmp = 1
#     i = 1
#     while abs(tmp) > acc / 10:
#         if i % 2 == 0:
#             tmp = 4 / den
#         else:
#             tmp = -4 / den
#         pi_acc += tmp
#         den += 2
#         i += 1
#     tmp = str(pi_acc)
#     print(tmp[:ln])
#
#
# accuracy = str(input('Input accuracy of PI :'))
# if float(accuracy) <= 0.1:
#     pi_accuracy(float(accuracy), len(accuracy))
# else:
#     print('Incorrect number')
#
#
#
# 2 variant
#
# import math
#
# num = float(input('Введите число от 10^{-10} до 10^{-1}: '))
# count = 0
# if num >= 10 ** (-10) and num <= 10 ** (-1): while
#     (num != 1): num *= 10
#     count += 1
#     x = str(round(math.pi, count + 1))
# print(f'Число π с соответствующим количеством знаков = {x[:(len(x) - 1)]}')
# print(f'Число π = {math.pi}') else: print('Ошибка!Введите число от 10^{-1} до ≤10^{-10}')

