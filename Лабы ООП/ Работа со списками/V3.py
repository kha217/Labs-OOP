array = [int(input(f"Введите элемент {i}: ")) for i in range(8)]

nechot = sum(array[i] for i in range(1, len(array), 2))

print("Массив:", *array)
print("Сумма элементов с нечетными индексами:", nechot)

#---------------------------------------------------------Second---------------------------------------------------------


D = [int(input(f"Введите элемент {i + 1}: ")) for i in range(int(8))]
D = [x * 2 if x < 15 else x for x in D]
print("Преобразованный массив:", D)