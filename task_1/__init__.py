# -*- coding: utf-8 -*- 


def fill_spiral_matrix(n):
    """ Создает мартицу размером n * n и заполняет ее по спирали

    Parameters
    ----------
    n : int
        Размерность матрицы.

    Returns
    -------
    list[list[int]]
        Матрица заполненная по спирали
    """
    matrix = [[0] * n for i in range(n)]

    def fill_list(start_position, length, number):
        position = start_position
        number += 1
        matrix[position[1]][position[0]] = number
        for i in range(4):
            direction, steps = [
                ((1, 0), length - 1),
                ((0, 1), length - 1),
                ((-1, 0), length - 1),
                ((0, -1), length - 2),
            ][i]
            while steps > 0:
                position = position[0] + direction[0], position[1] + direction[1]
                steps -= 1
                number += 1
                matrix[position[1]][position[0]] = number

        if length > 2:
            fill_list(start_position=(start_position[0] + 1, start_position[1] + 1), length=length - 2, number=number)

    fill_list(start_position=(0, 0), length=n, number=0)

    return matrix
