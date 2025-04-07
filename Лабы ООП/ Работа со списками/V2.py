array = [int(input(f"Введите элемент {i}: ")) for i in range(int(input("Введите количество элементов в массиве: ")))]
min_array = array.index(min(array))
print(f'Минимальный элемент: {min_array}')


#---------------------------------------------------------Second---------------------------------------------------------

array2 = [int(input(f"Введите элемент {i}: ")) for i in range(int(input("Введите количество элементов в массиве: ")))]

positive_array = [x for x in array2 if x > 0]  # Положительные элементы
non_positive_array = [x for x in array2 if x <= 0]  # Неположительные элементы

print("Положительные элементы:", positive_array)
print("Неположительные элементы:", non_positive_array)