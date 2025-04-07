print(f'\n{'Варианта 2':^50}\n {'Задание №2':^49}\n')

n = int(input("Введите размер квадратной матрицы n: "))

print("Введите элементы матрицы построчно (через пробел):")
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]

print("Измененная матрица:")
for row in matrix:
    print(" ".join(map(str, row)))
