print(f'\n{'Варианта 4':^50}\n {'Задание №2':^49}\n')


N = int(input("Введите количество строк и столбцов матрицы 'N': "))
matrix = []

print("Введите элементы матрицы построчно (через пробел):")
for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

new_matrix = [[1 if matrix[i][j] > 0 else 0 for j in range(N)] for i in range(N)]

print("Нижняя треугольная матрица:")
for i in range(N):
    for j in range(N):
        if i >= j:
            print(new_matrix[i][j], end=' ')
        else:
            print(' ', end=' ')
        print()