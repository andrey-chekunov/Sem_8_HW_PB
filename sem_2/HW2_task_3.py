# Задайте список из n чисел последовательности (1+ (1/n))^n
# и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55


n = int(input('Enter the number N: '))
lst = [round((1+1/i)**i, 2) for i in range(1, n+1)]
print(f'Sequence of numbers: {lst}\nSum of numbers: {round(sum(lst), 2)}')