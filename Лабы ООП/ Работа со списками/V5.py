from itertools import count

array = [int(input(f"Введите элемент {i + 1}: ")) for i in range(10)]
negative = []
for i in range(len(array) - 1):
    if array[i] < 0 and array[i + 1] < 0:
        negative.append((array[i], array[i + 1]))

if negative:
    print('Пары отрицательных чисел, стоящих рядом:')
    for neg in negative:
        print(*neg)
else:
    print("Нет пар отрицательных чисел, стоящих рядом.\n")


print('\n2 способ\n')



negative1 = [(array[i], array[i + 1]) for i in range(len(array) - 1) if array[i] < 0 and array[i + 1] < 0]

print("Пары отрицательных чисел, стоящих рядом:" + ''.join([f"\n{neg1[0]}, {neg1[1]}" for neg1 in negative1]) if negative1 else "Нет пар отрицательных чисел, стоящих рядом.")


#---------------------------------------------------------Second---------------------------------------------------------

array2 = [int(input(f"Введите элемент {i + 1}: ")) for i in range(10)]
uniqueness = []
[uniqueness.append(i) for i in array2 if i not in uniqueness]
print(*uniqueness)