"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

"""


class ComplexNumber:
    def __init__(self, complex_list):
        self.complex_list = complex_list

    def __add__(self, other):
        return [x + y for x, y in zip(self.complex_list, other.complex_list)]

    def __mul__(self, other):
        self.real_part_list = [x * y for x, y in zip(self.complex_list, other.complex_list)]
        self.real_part = self.real_part_list[0] - self.real_part_list[1]
        self.temp = other.complex_list[0]
        other.complex_list[0] = other.complex_list[1]
        other.complex_list[1] = self.temp
        self.imaginary_part_list = [x * y for x, y in zip(self.complex_list, other.complex_list)]
        self.imaginary_part = self.imaginary_part_list[0] + self.imaginary_part_list[1]
        return f'{self.real_part} + {self.imaginary_part}'


complex_1 = ComplexNumber([1, -2])
complex_2 = ComplexNumber([2, 1])
print(complex_1 + complex_2)
print(complex_1 * complex_2)

"""
PS.
Красоту по выводу информации не успел сделать.
Сама логика программы работает.  
"""
