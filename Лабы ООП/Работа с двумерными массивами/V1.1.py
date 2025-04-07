print(f'\n{'Варианта 1':^50}\n {'Задание №1':^49}\n')


N = int(input("Введите размер матрицы N: "))

matrix = []

print("Введите элементы матрицы построчно (через пробел):")
for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

sum_positive, count_positive = 0, 0

for i in range(N):
    for j in range(i + 1, N):
        if matrix[i][j] > 0:
            sum_positive += matrix[i][j]
            count_positive += 1

print(f"Сумма положительных элементов над главной диагональю: {sum_positive}")
print(f"Количество положительных элементов над главной диагональю: {count_positive}")
