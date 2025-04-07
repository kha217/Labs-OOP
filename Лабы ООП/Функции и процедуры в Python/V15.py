# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrom(n):
    dvoich = bin(n)[2:]
    return dvoich == dvoich[::-1]


def dvoich_palindromes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i) and is_palindrom(i):
            primes.append(i)
    return primes


n = int(input("Введите натуральное число n: "))
result = dvoich_palindromes(n)
print(f"Простые числа ≤ {n}, двоичная запись которых — палиндром:", *result)

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')


def calculate_distance(point1, point2):

    return ((point1[0] - point2[0]) ** 2 +
            (point1[1] - point2[1]) ** 2 +
            (point1[2] - point2[2]) ** 2) ** 0.5


def find_min_distance(points):
    closest_pairs = []
    point_names = ['X', 'Y', 'Z', 'T']

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = calculate_distance(points[i], points[j])

            if min_distance is None or dist < min_distance:
                min_distance = dist
                closest_pairs = [(point_names[i], point_names[j])]
            elif dist == min_distance:
                closest_pairs.append((point_names[i], point_names[j]))

    return min_distance, closest_pairs


def input_point(name):
    while True:
        try:
            coords = input(f"Введите координаты точки {name} (x y z через пробел): ").split()
            if len(coords) != 3:
                print("Ошибка: нужно ввести 3 координаты")
                continue
            return [float(coord) for coord in coords]
        except ValueError:
            print("Ошибка: координаты должны быть числами")



points = []
point_names = ['X', 'Y', 'Z', 'T']

for name in point_names:
    points.append(input_point(name))

min_dist, pairs = find_min_distance(points)

print(f"\nМинимальное расстояние: {min_dist:.4f}")
print("Пары точек с минимальным расстоянием:")
for pair in pairs:
    print(f"{pair[0]} и {pair[1]}")
