print(f'\n{'Варианта 4':^50}\n {'Задание №1':^49}\n')

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

max_row = min_row = matrix[0]
max_sum = min_sum = sum(max_row)

for row in matrix[1:]:
    row_sum = sum(row)
    if row_sum > max_sum:
        max_sum, max_row = row_sum, row
    if row_sum < min_sum:
        min_sum, min_row = row_sum, row

print(f"Строка с наибольшей суммой: {max_row}, сумма: {max_sum}")
print(f"Строка с наименьшей суммой: {min_row}, сумма: {min_sum}")
