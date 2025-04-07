array = [int(input(f"Введите элемент {i}: ")) for i in range(int(input("Введите количество элементов в массиве: ")))]
print(f'Максимальный элемент: {max(array)}\nПорядковый номер {array.index(max(array)) + 1}')

# ---------------------------------------------------------Second---------------------------------------------------------


array2 = [int(input(f"Введите элемент {i}: ")) for i in range(5)]
# 1 Способ
nechot = [i for i in array2 if i % 2 == 1]
if nechot:
    nechot.sort(reverse=True)
    print("Массив нечетных чисел в порядке убывания:", nechot)
else:
    print("Нечетных чисел в массиве нет.")

# 2 Способ
# array2 = [int(input(f"Введите элемент {i}: ")) for i in range(5)]

# if (nechot := sorted((i for i in array2 if i % 2 != 0), reverse=True)):
# print("Массив нечетных чисел в порядке убывания:", nechot)
# else:
# print("Нечетных чисел в массиве нет.")
