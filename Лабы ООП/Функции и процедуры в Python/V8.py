# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def find_numbers(n):
    result = []
    for num in range(1, n + 1):
        digits = [int(d) for d in str(num)]
        if 0 in digits:
            continue
        if all(num % d == 0 for d in digits):
            result.append(num)
    return result


n = int(input("Введите число n: "))
print("Числа, которые делятся на каждую из своих цифр:", find_numbers(n))

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')


def first_later(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]

array = [int(input(f"Введите элемент {i + 1}: ")) for i in range(int(input("Введите длину массива: ")))]

print(f"Исходный массив array: {array}")
first_later(array)
print(f"Изменённый массив array: {array}")
