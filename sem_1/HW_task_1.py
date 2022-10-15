# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day=int(input('Enter a number indicating the day of the week: '))
if (day==6 or day==7):
    print('YES! Weekend')
elif (1<=day and day<=5):
    print('NO! Weekday')
else:
    print('Wrong! Enter a number indicating the day of the week')