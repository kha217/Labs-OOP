# ---------------------------------------------------------First---------------------------------------------------------
print('Задание №1')


def subtract_fractions(A, B, C, D):
    chislitel = A * D - C * B  # числитель
    znamenatel = B * D  # знаменатель

    # Находим НОД
    a, b = chislitel, znamenatel
    while b:
        a, b = b, a % b
    common_divisor = a

    chislitel //= common_divisor
    znamenatel //= common_divisor

    return chislitel, znamenatel


A = 1
B = 2
C = 3
D = 4


res_chislitel, res_znamenatel = subtract_fractions(A, B, C, D)

if res_znamenatel < 0:
    res_chislitel = -res_chislitel
    res_znamenatel = -res_znamenatel

res_chislitel, res_znamenatel = subtract_fractions(A, B, C, D)
print(f"Результат вычитания дроби {A}/{B} и дроби {C}/{D} = {res_chislitel}/{res_znamenatel}")
# ---------------------------------------------------------Second---------------------------------------------------------
print('\nЗадание №2\n')


def find_divisors(n):
    a = [i for i in range(1, n + 1) if n % i == 0]
    print(f'Все делители числа {n}:', *a)


find_divisors(int(input()))
