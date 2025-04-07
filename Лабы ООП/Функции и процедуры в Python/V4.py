# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def divide_fractions(A, B, C, D):
    chislitel = A * D  # числитель
    znamenatel = B * C  # знаменатель

    # Находим НОД
    a, b = chislitel, znamenatel
    while b:
        a, b = b, a % b
    common_divisor = a

    chislitel //= common_divisor
    znamenatel //= common_divisor

    return chislitel, znamenatel


A = 1
B = 2
C = 3
D = 4

res_chislitel, res_znamenatel = divide_fractions(A, B, C, D)
print(f"Результат деления дроби {A}/{B} на дробь {C}/{D} = {res_chislitel}/{res_znamenatel}")

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')


def is_point_inside_circle(a, b, R, point):
    x, y = point
    return (x - a) ** 2 + (y - b) ** 2 < R ** 2

def count_points_inside_circle(a, b, R, points):
    count = 0
    for point in points:
        if is_point_inside_circle(a, b, R, point):
            count += 1
    return count


a = 0
b = 0
R = 5


points = [(1, 1), (6, 6), (3, 4), (-1, -1), (0, 0)]
inside_count = count_points_inside_circle(a, b, R, points)
print(f"Количество точек, лежащих внутри окружности: {inside_count}")
