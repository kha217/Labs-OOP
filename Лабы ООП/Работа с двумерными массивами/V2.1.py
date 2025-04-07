print(f'\n{'Варианта 2':^50}\n {'Задание №1':^49}\n')

def is_magic_square(matrix): # Функиция для проверки
    n = len(matrix)
    magic_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_sum:
            return False
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False
    if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False
    return True


n = int(input("Введите размер квадратной матрицы n: "))
matrix = []

print("Введите элементы матрицы построчно (через пробел):")
#matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
if is_magic_square(matrix):
    print("Матрица является магическим квадратом.")
else:
    print("Матрица не является магическим квадратом.")
