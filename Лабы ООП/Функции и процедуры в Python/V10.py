# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def count_numbers(n, a, b, c):
    allowed_digits = {str(a), str(b), str(c)}
    count = 0
    for i in range(100, n + 1):
        i_str = str(i)
        if all(j in allowed_digits for j in i_str):
            count += 1
    return count


n = int(input('Введите число n(по условию 210 < N < 231): '))
a, b, c = map(int, input("Введите три цифры через пробел: ").split())

print(f"Количество чисел от 100 до {n}, состоящих из цифр {a}, {b}, {c}: {count_numbers(n, a, b, c)}")

# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')



def string_revers(words):
    st = words.split()
    reversed_words = st[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string


input_string = input('Введите слова(например: "Привет, как дела?"): ')
reversed_string = string_revers(input_string)
print(f"Исходная строка: {input_string}")
print(f"Обратная строка: {string_revers(input_string)}")