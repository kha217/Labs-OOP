array = [int(input(f"Введите элемент {i + 1}: ")) for i in range(10)]
count_more = sum(1 for i in array if i > max(array))
count_less = sum(1 for i in array if i < max(array))
print("Максимальный элемент:", max(array),
      "\nКоличество меньших максимального элемента:", count_less,
      "\nКоличество больших максимального элемента:", count_more)


#---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')

summa_more_five = sum(i for i in array if i >5)
print('Сумма чисел, которые больше 5:', summa_more_five)
