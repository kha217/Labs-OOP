print(f'\n{'Варианта 4':^50}\n {'Задание №1':^49}\n')

n, m = map(int, input("Введите количество строк 'n' и количество столбцов 'm' матрицы (через пробел): ").split())
matrix = []

print("Введите элементы матрицы построчно (через пробел):")
for i in range(n):
    while True:
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        if len(row) == m:
            matrix.append(row)
            break
        else:
            print(f"Ошибка: строка должна содержать {m} элементов. Пожалуйста, введите строку снова.")

for i in range(n):
    matrix[i].sort()

print("Упорядоченная матрица:")
for row in matrix:
    print(" ".join(map(str, row)))