# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

array_size = int(input("Введите сколько чисел должно быть в списке: "))
amount_fraction = array_size - 1
fraction_number = [round(random.uniform(1.1, 12.9), 2)
for fraction_number in range(amount_fraction)]

from random import randint
integer_numbers = []
for i in range(array_size - amount_fraction):
    integer_numbers.append(randint(1, 10))
    all_number = integer_numbers + fraction_number
    random.shuffle(all_number)

print("Список вещественных чисел", all_number)
a = 0
i = 0
while a < len(all_number):
    all_number[a] = (all_number[a] - int(all_number[a]))
    all_number[i] = all_number[a]
    i += 1
    a += 1
print("Готовый список, только дробная часть:", sorted(all_number))

new_list = []
for i in range(len(all_number)):
    if all_number[i] > 0:
        new_list.append(all_number[i])
        print("Список без нулевого значения", new_list)
        resyylt = max(new_list) - min(new_list)
print("Разница между максимальным и минимальным и значением дробной части элементов", round(resyylt, 2))






list1 = [1.1, 1.2, 3.1, 5, 10.01]
new_list = [round(i%1, 2) for i in list1 if i%1 != 0]
# print(new_list) создаем новый лист только с дробной частью, убираем нулевые значения
print(f"Разницу между максимальным и минимальным значением дробной части элементов: {max(new_list) - min(new_list)}") # выводим разницу между максимальным и минимальным значением