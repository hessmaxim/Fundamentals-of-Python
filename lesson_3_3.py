# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(x, y, z):
    my_list = [x, y, z]
    num_min = min(my_list)
    my_list.remove(num_min)
    sum_num = my_list[0] + my_list[1]
    return sum_num


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
print(my_func(num1, num2, num3))
