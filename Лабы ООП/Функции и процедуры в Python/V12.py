# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def sum_of_divisors(n):
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total


def friendly_numbers(n):
    friendly_pairs = []
    for a in range(1, n + 1):
        b = sum_of_divisors(a)
        if b > a and b <= n:
            if sum_of_divisors(b) == a:
                friendly_pairs.append((a, b))

    return friendly_pairs

n = int(input("Введите натуральное число n: "))
print(f"Пары дружественных чисел, не превышающих {n}:")
pairs = friendly_numbers(n)
for pair in pairs:
    print(*pair)

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')


def calculate_median(a, b, c):
    return (1 / 2) * ((2 * b ** 2 + 2 * c ** 2 - a ** 2) ** 0.5)


def medians_of_triangle(a, b, c):
    medians_a = calculate_median(a, b, c)
    medians_b = calculate_median(b, a, c)
    medians_c = calculate_median(c, a, b)
    return medians_a, medians_b, medians_c


def medians_of_median_triangle(medians_a, medians_b, medians_c):
    medians_median_a = calculate_median(medians_a, medians_b, medians_c)
    medians_median_b = calculate_median(medians_b, medians_a, medians_c)
    medians_median_c = calculate_median(medians_c, medians_a, medians_b)
    return medians_median_a, medians_median_b, medians_median_c


a, b, c = map(float, input('Введите длину сторон A, B и C через пробел: ').split())

medians = medians_of_triangle(a, b, c)
print(f"Медианы исходного треугольника: {medians[0]}, {medians[1]}, {medians[2]}")

median_medians = medians_of_median_triangle(*medians)
print(
    f"Медианы треугольника, стороны которого - медианы исходного: {median_medians[0]}, {median_medians[1]}, {median_medians[2]}")



