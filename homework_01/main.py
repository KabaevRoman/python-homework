"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    temp = []
    for num in args:
        temp.append(num * num)
    return temp


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    flag = True
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break
    else:
        flag = False
    return flag


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    filtered_list = []
    if filter_type == ODD:
        for num in numbers:
            if num % 2 != 0:
                filtered_list.append(num)
    elif filter_type == EVEN:
        for num in numbers:
            if num % 2 == 0:
                filtered_list.append(num)
    elif filter_type == PRIME:
        for num in numbers:
            if is_prime(num):
                filtered_list.append(num)
    return filtered_list
