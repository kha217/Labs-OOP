print(f'\n{'Варианта 3':^50}\n {'Задание №1':^49}\n')


def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


n = int(input("Введите размер квадратной матрицы n: "))

print("Введите элементы матрицы построчно (через пробел):")
matrix = [list(map(int, input().split())) for _ in range(n)]

if is_symmetric(matrix):
    print("Матрица является симметричной.")
else:
    print("Матрица не является симметричной.")
