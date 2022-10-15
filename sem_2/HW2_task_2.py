# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Enter the number N: '))
# multi = 1
# print('[', end=' ')                         #Чисто для красоты
# for i in range(1, n+1):
#     multi *= i
#     print(multi, end=' ')
# print(']')                                  #Чисто для красоты


import math
print(math.factorial(n))
