# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x= float(input('Enter the X ≠ 0: '))
y= float(input('Enter the Y ≠ 0: '))
if (x>0 and y>0):
    print('The number of the quarter plane is: 1st')
if(x<0 and y>0):
    print('The number of the quarter plane is: 2nd')
if(x<0 and y<0):
    print('The number of the quarter plane is: 3rd')
if(x>0 and y<0):
    print('The number of the quarter plane is: 4th')
if(x==0 and y==0):
    print('WRONG! Enter the X ≠ 0 and Y ≠ 0')