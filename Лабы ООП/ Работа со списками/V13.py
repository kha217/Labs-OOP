numbers = [1, 22, 3, 24, 2, 18, 3, 1, ]

duplicates = []

for i in range(len(numbers)):
    if numbers[i] not in duplicates:
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.append(numbers[i])
                break

for value in duplicates:
    indices = []
    for index, num in enumerate(numbers):
        if num == value:
            indices.append(index)
    print(f"Элемент {value} встречается на индексах: {indices}")

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')

num = [x * 2 if x < 15 else x for x in numbers]
print("Преобразованный массив:", num)
