# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def count_divisors(num):
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    return count


def numbers_with_most_divisors(M, N):
    max_divisors = 0
    numbers_with_max_divisors = []

    for num in range(M, N + 1):
        divisors_count = count_divisors(num)

        if divisors_count > max_divisors:
            max_divisors = divisors_count
            numbers_with_max_divisors = [num]
        elif divisors_count == max_divisors:
            numbers_with_max_divisors.append(num)

    return numbers_with_max_divisors, max_divisors


M = int(input("Введите значение M: "))
N = int(input("Введите значение N: "))

numbers, max_divs = numbers_with_most_divisors(M, N)

print(f"Числа в интервале [{M}, {N}] с наибольшим количеством делителей {max_divs}: {numbers}")

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')

import math


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def find_max_distance(points):
    max_distance = 0
    point_pair = (None, None)

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = calculate_distance(points[i], points[j])
            if distance > max_distance:
                max_distance = distance
                point_pair = (points[i], points[j])

    return max_distance, point_pair


X = (float(input("Введите координаты точки X (x1, x2): ")))
Y = (float(input("Введите координаты точки Y (y1, y2): ")))
Z = (float(input("Введите координаты точки Z (z1, z2): ")))
P = (float(input("Введите координаты точки P (p1, p2): ")))

points = [X, Y, Z, P]
max_distance, point_pair = find_max_distance(points)

print(f"Максимальное расстояние: {max_distance:.2f}")
print(f"Точки, находящиеся на максимальном расстоянии: {point_pair[0]} и {point_pair[1]}")
