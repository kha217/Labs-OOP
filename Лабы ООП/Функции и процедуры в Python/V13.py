# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    n = len(digits)
    sum_of_powers = sum(d ** n for d in digits)
    return sum_of_powers == number

def find_armstrong_numbers(k):
    armstrong_numbers = []
    for num in range(1, k + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

k = int(input("Введите число k: "))

result = find_armstrong_numbers(k)
print(f"Числа Армстронга от 1 до {k}:")
print(result)

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')

import math

def find_min_angle_point(points):
    min_angle = float('inf')
    min_point = None

    for point in points:
        x, y = point
        angle = math.atan2(y, x)
        angle_degrees = math.degrees(angle)

        if angle_degrees < min_angle:
            min_angle = angle_degrees
            min_point = point

    return min_point


X = (float(input("Введите координаты точки X (x1, x2): ")))
Y = (float(input("Введите координаты точки Y (y1, y2): ")))
Z = (float(input("Введите координаты точки Z (z1, z2): ")))

points = [X, Y, Z]
min_point = find_min_angle_point(points)

print(f"Координаты точки с минимальным углом: {min_point}")

