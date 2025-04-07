# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def nod(a, b):
    while b:
        a, b = b, a % b
    return a


def nok(a, b):
    return (a * b) // nod(a, b)


a, b = int(input()), int(input())

print(f"НОД({a}, {b}) = {nod(a, b)}")
print(f"НОК({a}, {b}) = {nok(a, b)}")

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')

import math

def area_quadrilateral(a, b, c, d, diagonal):
    p = (a + b + c + d) / 2
    area1 = math.sqrt((p - a) * (p - b) * (p - c) * (p - d)) #math.sqrt() для возврашения квадратного корня числа.

    area2 = 0.5 * diagonal * math.sqrt((p - a) * (p - b) * (p - diagonal))
    area3 = 0.5 * diagonal * math.sqrt((p - c) * (p - d) * (p - diagonal))

    return area1 + area2 + area3


a, b = float(input("Введите длину первой стороны (a): ")), float(input("Введите длину второй стороны (b): "))
c, d = float(input("Введите длину третьей стороны (c): ")), float(input("Введите длину четвертой стороны (d): "))
diagonal = float(input("Введите длину диагонали: "))

area = area_quadrilateral(a, b, c, d, diagonal)
print(f"Площадь выпуклого четырехугольника = {area:.2f}")
