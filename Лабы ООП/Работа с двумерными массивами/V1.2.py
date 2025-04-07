print(f'\n{'Варианта 1':^50}\n {'Задание №2':^49}\n')


N, M = map(int, input("Введите количество строк матрицы 'N' и количество столбцов матрицы 'M':").split())
matrix = []
print("Введите элементы матрицы построчно (через пробел):")
for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(N):
    if M > 0:
        max_value = matrix[i][0]
        min_value = matrix[i][0]
        max_index = 0
        min_index = 0

        for j in range(M):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_index = j
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_index = j

        matrix[i][max_index], matrix[i][0] = matrix[i][0], matrix[i][max_index]

        matrix[i][min_index], matrix[i][-1] = matrix[i][-1], matrix[i][min_index]

print("Измененная матрица:")
for row in matrix:
    print(" ".join(map(str, row)))
