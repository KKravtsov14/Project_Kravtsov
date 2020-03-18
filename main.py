import time as t
import random as r


def cycle(lst, number):

    """

    :param lst:
    :param number:
    :return:
    """

    center = len(lst) // 2
    left_border = 0
    right_border = len(lst) - 1

    while left_border <= right_border:
        center = (left_border + right_border) // 2
        if number < lst[center]:
            right_border = center - 1
        elif number > lst[center]:
            left_border = center + 1
        else:
            return center
    else:
        return


def recursion(lst, number, left_border, center, right_border):

    """

    :param lst:
    :param number:
    :param left_border:
    :param center:
    :param right_border:
    :return:
    """

    if left_border <= right_border:
        if number == lst[center]:
            return center
        elif number < lst[center]:
            return recursion(lst, number, left_border, (left_border + center - 1) // 2, center - 1)
        elif number > lst[center]:
            return recursion(lst, number, center + 1, (center + 1 + right_border) // 2, right_border)
    else:
        return


def main():
    lst = []
    for i in range(r.randint(-10000, 10000)):
        lst.append(r.randint(-10000, 10000))
    lst.sort()

    number = int(input())

    count_start = t.perf_counter()
    program_result = cycle(lst, number)
    count_end = t.perf_counter()

    print(program_result, 'Время работы цикла:', '{:.10f}'.format(count_end - count_start))

    count_start = t.perf_counter()
    program_result = recursion(lst, number, 0, len(lst) // 2, len(lst) - 1)
    count_end = t.perf_counter()

    print(program_result, 'Время работы рекурсии:', '{:.10f}'.format(count_end - count_start))
    print('Время выполнения всей программы:', t.perf_counter())


main()