# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint
array_size = int(input("Введите сколько чисел должно быть в списке: "))
numbers = []
for i in range(array_size):
   numbers.append(randint(1, 10))
print("Заданный список рандомных чисел:", numbers)
ln = len(numbers)
for i in range(ln):
   if i >= ln/2:
      break
   print(numbers[i] * numbers[-i-1], end=' ')

