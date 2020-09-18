"""

5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().

"""

from functools import reduce


def reducer_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev * el


my_list = [el for el in range(100, 1001, 2)]
print(my_list)
mul_el = reduce(reducer_func, my_list)
print(mul_el)
