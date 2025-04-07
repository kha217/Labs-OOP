numbers = [1, 2, 3, 4, 2, 5, 3, 1, 6, 7, 8, 6]

duplicates = []


for i in range(len(numbers)):
    if numbers[i] not in duplicates:
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.append(numbers[i])
                break

if duplicates:
    print("Повторяющиеся элементы:", duplicates)
else:
    print("Повторяющихся элементов нет.")


# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

odd_num = reversed([i for i in numbers if i % 2 != 0])

if odd_num:
    print("Нечетные числа в порядке убывания:", odd_num)
else:
    print("Нечетных чисел нет.")