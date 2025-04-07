array = [int(input(f"Введите элемент {i}: ")) for i in range(int(input("Введите количество элементов в массиве: ")))]
summ_even = sum(array)

proiz = 1
for i in range(len(array)):
    proiz *= array[i]

print("Сумма элементов :", summ_even,
      "\nПроизведение элементов:", proiz)


#---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')

avg = sum(array) / len(array)
array2 = [avg if x == 0 else x for x in array]
print("Измененный массив:", array2)