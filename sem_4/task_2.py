# Найдите корни квадратного уравнения Ax² + Bx + C = 0

a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
d = b ** 2 - 4 * a * c
print(f'Discriminant = {d}')
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(x1, x2)
elif d == 0:
    x1 = -b / (2 * a)
    print(x1)
else:
    print('Don"t have resolve')