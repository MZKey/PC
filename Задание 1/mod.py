from numpy import random as rn
import numpy as np


def calc677(n):
    """
    Решение 677 задачи

    :param n: размерность матрицы
    """
    a = np.ones((n, n), dtype=int)
    print(a)
    b = np.zeros((n, n), dtype=int)

    for i in range(n):
        for j in range(n):
            summ = 0
            summ += a[0:i, 0:j].sum()  # вверхний левый
            summ += a[0:i, j + 1:n].sum()  # вверхний правый
            summ += a[i + 1:n, 0:j].sum()  # нижний левый
            summ += a[i + 1:n, j + 1:n].sum()  # нижний правый
            # b[i][j] = a + b+ c+d
            b[i][j] = summ
    return (b)


def lab8(n):
    """
    Получение матрицы элемент, к-ой равен сумме элементов данной матрицы
    расположенных в области, как на рисунке
    :param n:
    :return:
    """
    a = np.ones((n, n), dtype=int)
    print(a)
    b = np.zeros((n, n), dtype=int)

    for i in range(n):
        for j in range(n):
            summ = 0
            summ = a[0:i + 1, j:n + 1].sum()  # ИСПОЛЬЗОВАТЬ [,]
            # print(a[0:i + 1, j:n + 1])
            # summ = a[n - i - 1:n][n - j - 1:n].sum()
            b[i][j] = summ
    return (b)


def calc335(n):
    """
    Решение 136 задачи

    Параметры:
    n -- количество итераций

    """
    s = 0
    for k in range(1, n + 1):
        c = 1
        for j in range(0, k + 1):
            c = c * (k + j)

        s += c
        print(f"k = {k:3}   res = {s}")

    return s


def calc136l(arr):
    """
    Решение 136 задачи

    Параметры:
    arr -- массив

    """
    res = arr[0]
    for i in range(1, len(arr)):
        res *= arr[i]

    res = abs(res)
    return res ** .5


def calc178e(arr):
    """
    Решение 136 задачи

    Параметры:
    arr -- массив

    """
    res = 0
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 != 0:
            res += 1

    return res


def init_array(arr):
    """
    Заполнение массива случайными числами или вручную

    Параметры:
    arr -- массив

    """

    print("\nЗаполнить массив случайными числами? Введите \"1\", если да или \"0\", если нет!")
    flag = int(input("flag = "))

    if flag == 1:
        arr = rn.randint(1, 10, len(arr), )
        # arr = rn.random(len(arr),)
        print("\na =", arr)
        return arr

    elif flag == 0:
        print()
        for i in range(len(arr)):
            arr[i] = float(input("a[{}] = ".format(i + 1)))
        return arr

    else:
        print("Вы ввели неккоректное значение, было решено заполнить массив случайными числами")
        arr = rn.randint(1, 10, len(arr), )
        # arr = rn.random(len(arr),)
        print("\na =", arr)
        return arr
