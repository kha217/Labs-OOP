numbers = [3, 5, 1, 8, 2, 7, 4, 6, 0, 9]

max_index = numbers.index(max(numbers))
min_index = numbers.index(min(numbers))

numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]
print("Измененный массив:", *numbers)



# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')


array = [int(input(f"Введите элемент {i + 1}: ")) for i in
         range(int(input("Введите количество элементов в массиве: ")))]


avg = sum(array) / len(array)

for i in range(len(array)):
    if array[i] > avg:
        array[i] = 1

print("Измененный массив:", *array)