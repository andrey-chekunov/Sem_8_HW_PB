# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst=[2, 3, 5, 9, 3]
plus=0
for i in range(1,len(lst),2):
    plus+=lst[i]
print(f'The sum of the list items in an odd position = {plus}')


# от Натальи
# lst = [2,3,5,9,3]
# sum = 0
# for i in range(len(lst)):
# if i%2 == 1:                              #Для всех нечетных И (тоже самое , практически что и у меня (строка8 - начиная с индекса 1, шаг 2)
# sum += lst[i]
# print(sum)

# from random import randint
# lst = []
# for i in range(randint(4,10)):              #Рандомно создается список от 4 до 10 элементов
# lst.append(randint(1,100))                  #Рандомно заполняет наш список числами от 1 до 100
# print(lst)
# sum = 0
# for i in range(len(lst)):
# if i%2 == 1:
# sum += lst[i]
# print(sum)