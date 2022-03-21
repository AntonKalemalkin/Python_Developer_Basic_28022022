"""
Домашнее задание №1
Функции и структуры данных
"""
from math import sqrt


def power_numbers(*argument):
    numbers_power = list(map(lambda x: x ** 2, argument))
    print("Список квадратных чисел = ", numbers_power)
    return


power_numbers(1, 2, 5, 7, 4)

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"
"""
   функция, которая на вход принимает список из целых чисел,
   и возвращает только чётные/нечётные/простые числа
   (выбор производится передачей дополнительного аргумента)"""


def filter_numbers(numbers: list, filter_type):
    if filter_type == "even":
        print("четные =", list(filter(lambda x: x % 2 == 0, numbers)))
    if filter_type == "odd":
        print("нечетные =", list(filter(lambda x: x % 2 != 0, numbers)))
    if filter_type == "prime":
        list_num = []
        for i in numbers:
            if i > 1:
                print("i = ", i)
                for j in range(2, int((sqrt(i)) + 1)):
                    print("j = ", j)
                    if i % j == 0:
                        break
                else:
                    list_num.append(i)
        print("Простые числа = ", list_num)
    return


filter_numbers([1, 2, 3], ODD)

filter_numbers([2, 3, 4, 5], EVEN)
