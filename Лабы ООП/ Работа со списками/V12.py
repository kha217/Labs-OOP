numbers = [12, 5, 8, 21, 34, 7, 18, 9, 4]

min_odd = [i for i in numbers if i % 2 == 1]

if min_odd:
    print("Наименьший нечетный элемент списка:", min(min_odd))
else:
    print("В списке нет нечетных элементов.")

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Исходный массив A:", *a,
      "\nИсходный массив B:", *b)

a, b = b, a

print("Преобразованный массив A:", *a,
      "\nПреобразованный массив B:", *b)
