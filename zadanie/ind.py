#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает
эту строку в список чисел и возвращает их сумму. Определите декоратор для этой функции,
который имеет один параметр start – начальное значение суммы. Примените декоратор
со значением start=5 к функции и вызовите декорированную функцию. Результат
отобразите на экране.
"""


def my_decorate(start):

    def wrapper(func):

        def wrapped(*message):
            summ = 0
            for i in message:
                summ += i
            summ += start
            func(summ)
        return wrapped

    return wrapper


@my_decorate(start=5)
def main(message):
    print("Сумма чисел со start: ", message)


if __name__ == '__main__':
    main(*list(map(int, input('Введите список чисел: ').split(' '))))
