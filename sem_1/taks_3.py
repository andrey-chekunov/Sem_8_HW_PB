# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

n = int(input('Enter the number: '))
for i in range(-n, n + 1):
    print(i, end=' ')  # end=' ' - таким образом вывод будет напечатан в одну строку, иначе, по умолчанию, всегда с новой строки вывод будет
