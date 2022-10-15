# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def prime_factors(n):
   i = 2
   lst_prime = []
   while i * i <= n:
       while n % i == 0:
           lst_prime.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       lst_prime.append(int(n))
   return lst_prime
num2 = int(input('Input N: '))
print(prime_factors(num2))
