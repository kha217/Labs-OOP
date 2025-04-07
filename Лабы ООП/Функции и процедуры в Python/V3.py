# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def calculate_hypotenuse(cathetus1, cathetus2):
    return (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5


a1, b1 = map(float, input("Введите катеты первого прямоугольного треугольника через пробел: ").split())

a2, b2 = map(float, input("Введите катеты первого прямоугольного треугольника через пробел: ").split())

print(f"Гипотенуза первого треугольника: {calculate_hypotenuse(a1, b1)}")
print(f"Гипотенуза второго треугольника: {calculate_hypotenuse(a2, b2)}")

if calculate_hypotenuse(a1, b1) > calculate_hypotenuse(a2, b2):
    print("Гипотенуза первого треугольника больше.")
elif calculate_hypotenuse(a1, b1) < calculate_hypotenuse(a2, b2):
    print("Гипотенуза второго треугольника больше.")
else:
    print("Гипотенузы равны.")


# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')

a = 'пвапв аываы ввввввфап'


def sort_letters_in_words(words):
    return ' '.join(''.join(sorted(word)) for word in words.split())


print(sort_letters_in_words(a))

