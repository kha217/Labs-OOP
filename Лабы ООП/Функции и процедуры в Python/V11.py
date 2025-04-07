# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def twin_primes(n):
    twins = []
    for p in range(n, 2 * n - 1):
        if is_prime(p) and is_prime(p + 2):
            twins.append((p, p + 2))
    return twins


n = int(input("Введите n: "))

print(f"Пары близнецов в {n}, {2 * n}:")
for pair in twin_primes(n):
    print(*pair)

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')

matrix_a = [
    [100, 32, 13],
    [44, 75, 65],
    [74, 8, 31]
]

matrix_b = [
    [99, 82, 74],
    [33, 53, 4],
    [32, 24, 16]
]


def max_element(matrix):
    max_val = matrix[0][0]
    max_pos = (0, 0)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_pos = (i, j)
    return max_val, max_pos


def swap_elements(matrix_a, matrix_b):
    max_a, pos_a = max_element(matrix_a)
    max_b, pos_b = max_element(matrix_b)

    matrix_a[pos_a[0]][pos_a[1]] = max_b
    matrix_b[pos_b[0]][pos_b[1]] = max_a


def print_matrix(matrix):
    for i in matrix:
        print(i)


print("Матрица A до замены:")
print_matrix(matrix_a)
print("\nМатрица B до замены:")
print_matrix(matrix_b)

swap_elements(matrix_a, matrix_b)

print("\nМатрица A до замены:")
print_matrix(matrix_a)
print("\nМатрица B до замены:")
print_matrix(matrix_b)
