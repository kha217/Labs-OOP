# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def area_of_rectangle(x, y):
    return x * y


def area_of_triangle(x, y):
    return (x * y) / 2


def area_of_quadrilateral(x, y, z, t):
    return area_of_rectangle(x, y) + area_of_triangle(z, t)


x, y, z, t = map(float, input("Введите длину сторон x, y, z и t через пробел: ").split())
# Вычисление площади
total_area = area_of_quadrilateral(x, y, z, t)
print(f"Площадь четырехугольника: {total_area:.2f}")

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')


def octal(n):
    print(f"{oct(n)[2:]:0>10}")


octal(int(input("Введите неотрицательное целое число: ")))
