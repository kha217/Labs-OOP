print(f'\n{'Варианта 3':^50}\n {'Задание №2':^49}\n')



n, m = map(int, input("Введите количество строк матрицы 'n' и количество столбцов матрицы 'm' (через пробел): ").split())
print("Введите элементы матрицы построчно (через пробел):")
matrix = [list(map(float, input().split())) for _ in range(n)]

max_value = float('-inf')
max_row, max_col = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row, max_col = i, j


if max_row != 0:
    matrix[0], matrix[max_row] = matrix[max_row], matrix[0]

if max_col != 0:
    for i in range(n):
        matrix[i][0], matrix[i][max_col] = matrix[i][max_col], matrix[i][0]

print("Измененная матрица:")
for row in matrix:
    print(' '.join(map(str, row)))










n, m = map(int, input("Введите количество строк матрицы 'n' и количество столбцов матрицы 'm':").split())
print("Введите элементы матрицы построчно (через пробел):")
matrix = [list(map(int, input().split())) for _ in range(n)]


max_row = next(i for i in range(n) if max(max(row) for row in matrix) in matrix[i])
max_col = matrix[max_row].index(max(max(row) for row in matrix))


matrix[0], matrix[max_row] = matrix[max_row], matrix[0]

for i in range(n):
    matrix[i][0], matrix[i][max_col] = matrix[i][max_col], matrix[i][0]

print("Измененная матрица:")
for row in matrix:
    print(" ".join(map(str, row)))



n, m = map(int, input("Введите количество строк матрицы 'n' и количество столбцов матрицы 'm':").split())

print("Введите элементы матрицы построчно (через пробел):")
matrix = [list(map(int, input().split())) for _ in range(n)]

max_value = float('-inf')
max_row = 0
max_col = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row = i
            max_col = j

matrix[0], matrix[max_row] = matrix[max_row], matrix[0]

for i in range(n):
    matrix[i][0], matrix[i][max_col] = matrix[i][max_col], matrix[i][0]

print("Измененная матрица:")
for row in matrix:
    print(" ".join(map(str, row))) # первоначальный код
