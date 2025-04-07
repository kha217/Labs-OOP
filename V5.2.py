n, m = map(int, input("Введите количество строк 'n' и количество столбцов 'm' матрицы (через пробел): ").split())
matrix = []

print("Введите элементы матрицы построчно (через пробел):")
for i in range(n):
    row = list(map(float, input(f"Строка {i + 1}: ").split()))
    if len(row) != m:
        print(f"Ошибка: строка должна содержать {m} элементов. Пожалуйста, введите строку снова.")
        i -= 1
        continue
    matrix.append(row)

new_matrix = []

for row in matrix:
    min_value = min(row)
    new_row = []
    for element in row:
        if element == min_value:
            if int(min_value) % 2 == 0:
                new_row.append(0)
            else:
                new_row.append(1)
        else:
            new_row.append(element)
    new_matrix.append(new_row)

print("Новая матрица:")
for row in new_matrix:
    print(" ".join(map(str, row)))