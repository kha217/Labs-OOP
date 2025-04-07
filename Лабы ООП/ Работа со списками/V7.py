array = [int(input(f"Введите элемент {i}: ")) for i in range(int(input("Введите количество элементов в массиве: ")))]
summ_even = sum(array[i] for i in range(0, len(array), 2) if i % 2 == 0)

proiz = 1
for i in range(len(array)):
    if i % 2 != 0:
        proiz *= array[i]

print("Сумма элементов с четными индексами:", summ_even)
print("Произведение элементов с нечетными индексами:", proiz)


#---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')

min_index = array.index(min(array))
max_index = array.index(max(array))

array[min_index], array[max_index] = array[max_index], array[min_index]

print("Массив после перестановки минимального и максимального элементов:", *array)