# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


x1 = int(input('Enter coordinates X1 of the point A: '))
y1 = int(input('Enter coordinates Y1 of the point A: '))
x2 = int(input('Enter coordinates X2 of the point B: '))
y2 = int(input('Enter coordinates Y2 of the point B: '))
dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# print('The distance between points in space = ', round(dist, 2))
print('A', (x1, y1), ';', 'B', (x2, y2), '->', round(dist, 2))              #Вот тут вопросик - можно ли как-то проще сделать запись вывода???
