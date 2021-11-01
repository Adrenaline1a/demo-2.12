#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает
эту строку в список чисел и возвращает их сумму. Определите декоратор для этой функции,
который имеет один параметр start – начальное значение суммы. Примените декоратор
со значением start=5 к функции и вызовите декорированную функцию. Результат
отобразите на экране.
"""


def decorate_function(func):
    start = 5

    def arg(message):
        summ = 0
        lst = message.split(' ')
        for i in lst:
            i = int(i)
            summ += i
        summ += start
        func(summ)
    return arg


@decorate_function
def main(message):
    print("Сумма чисел со start=5: ", message)


if __name__ == '__main__':
    main(input('Введите целые числа через пробел: '))
