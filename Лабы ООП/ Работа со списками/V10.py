array = [int(input(f"Введите элемент {i + 1}: ")) for i in
         range(int(input("Введите количество элементов в массиве: ")))]

duplicat = []

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] == array[j] and array[i] not in duplicat:
            duplicat.append(array[i])

print("Повторяющиеся элементы:", *duplicat) if duplicat else print("Повторяющихся элементов нет.")


# ---------------------------------------------------------Second---------------------------------------------------------


array = [10, 12, 13, 4, 5, 6, 7, 8, 9, 20, 111, 22, 43, 34, 51]

array2 = [0 if i < 10 else 1 if i > 20 else i for i in array]

print("Преобразованный массив:", *array,
      "\nПреобразованный массив:", *array2)