import numpy as np
from scipy.optimize import minimize_scalar


def matrix_multiplication(matrix_a, matrix_b):
    """
    Задание 1. Функция для перемножения матриц с помощью списков и циклов.
    Вернуть нужно матрицу в формате списка.
    """
    rows_a = len(matrix_a)
    cols_b = len(matrix_b[0])
    cols_a = len(matrix_a[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]


    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


def functions(a_1, a_2):
    if a_1 == a_2:
        return None
    a_1 = list(map(float, a_1.split()))
    a_2 = list(map(float, a_2.split()))

    def func1(x):
        return a_1[0] * x ** 2 + a_1[1] * x + a_1[2]

    def func2(x):
        return a_2[0] * x ** 2 + a_2[1] * x + a_2[2]

    extrema1 = minimize_scalar(func1)
    extrema2 = minimize_scalar(func2)

    roots = np.poly1d([a_1[0] - a_2[0], a_1[1] - a_2[1], a_1[2] - a_2[2]]).roots
    roots = [int(x) for x in roots]
    if len(roots) > 0:
        return sorted([(x, int(func1(x))) for x in roots])
    else:
        return []






def skew(x):
    """
    Задание 3. Функция для расчета коэффициента асимметрии.
    Необходимо вернуть значение коэффициента асимметрии, округленное до 2 знаков после запятой.
    """
    n = len(x)
    mean_x = sum(x) / n

    # Вычисляем числитель и знаменатель
    n1 = sum((xi - mean_x) ** 3 for xi in x) / n
    n2 = (sum((xi - mean_x) ** 2 for xi in x) / n) ** 1.5

    if n2 == 0:
        return None;

    return round(n1 / n2, 2)


def kurtosis(x):
    """
    Задание 3. Функция для расчета коэффициента эксцесса.
    Необходимо вернуть значение коэффициента эксцесса, округленное до 2 знаков после запятой.
    """
    n = len(x)
    mean_x = sum(x) / n

    n1 = sum((xi - mean_x) ** 4 for xi in x) / n
    n2 = (sum((xi - mean_x) ** 2 for xi in x) / n) ** 2

    if n1 == 0:
        return None;

    kurt = n1 / n2 - 3

    return round(kurt, 2)
