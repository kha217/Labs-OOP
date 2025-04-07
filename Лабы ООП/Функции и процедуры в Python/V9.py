# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def sum_of_digit(num):
    return sum(int(i) for i in str(num))


def steps(n):
    count = 0
    while n > 0:
        n -= sum_of_digit(n)
        count += 1
    return count


print(f"Количество шагов до нуля: {steps(int(input("Введите натуральное число: ")))}")

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')


array1 = [1, 2, 3, 4]
array2 = [5, 6, 7]
array3 = [10, 20, 30, 40, 50]


def product_of_numbers(arr):
    product = 1
    for i in arr:
        product *= i
    avg = sum(arr) / len(arr)
    print(f"Произведение элементов: {product}")
    print(f"Среднее арифметическое: {avg}")

product_of_numbers(array1)
product_of_numbers(array2)
product_of_numbers(array3)