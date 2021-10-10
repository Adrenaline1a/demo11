#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(number):
    try:
        ls = []
        x = 1
        while x < number + 1:
            """Создание списка [1, .., N]"""
            ls.append(x)
            x += 1
        for i in ls:
            print(ls[i-1:])
        """Запуск рекурсии"""
        return main(number-1)
    except RecursionError:
        exit()


if __name__ == '__main__':
    number = int(input('Введите N: '))
    main(number)
