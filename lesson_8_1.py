"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, line):
        self.line = line

    # def pr(self):
    #     return self.line

    @classmethod
    def transformation(cls, line):
        int_list = line.split('-')
        for i, item in enumerate(int_list):
            int_list[i] = int(item)
        return int_list

    @staticmethod
    def validation(int_list):
        if len(int_list) != 3:
            print('Некорректная дата.')
        if int_list[0] > 31 or int_list[0] == 0:
            print('Не правильно ввели день месяца.')
        if int_list[1] > 12 or int_list[1] == 0:
            print('Не правильно ввели номер месяца.')
        if int_list[2] > 9999:
            print('Не правильно ввели год.')


user = input('Введите дату в формате «день-месяц-год»: ')
D = Date(user)
new_ = D.transformation(user)
print(new_)
D.validation(new_)
