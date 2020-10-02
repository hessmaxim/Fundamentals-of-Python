"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, scanner, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""


class Office:
    def __init__(self, dict_):
        self.dict_ = dict_

    def __str__(self):
        return f"{self.dict_}"


class Equipment:
    def __init__(self, quantity):
        self.quantity = quantity


class Printer(Equipment):
    def __init__(self, brand, quantity):
        super().__init__(quantity)
        self.brand = brand

    def out_printer(self):
        self.brand = 'Принтер'
        return {self.brand: self.quantity}


class Scanner(Equipment):
    def __init__(self, brand, quantity):
        super().__init__(quantity)
        self.brand = brand

    def out_scanner(self):
        self.brand = 'Сканер'
        return {self.brand: self.quantity}


class Xerox(Equipment):
    def __init__(self, brand, quantity):
        super().__init__(quantity)
        self.brand = brand

    def out_xerox(self):
        self.brand = 'Ксерокс'
        return {self.brand: self.quantity}


Store = {}
while True:
    num_print = input('Введите количество принтеров, поступивших на склад: ')
    if num_print.isdigit():
        break
    else:
        print('Введите число цифрами!')
Store_P = Printer(1, num_print)
Store.update(Store_P.out_printer())
while True:
    num_scan = input('Введите количество сканеров, поступивших на склад: ')
    if num_scan.isdigit():
        break
    else:
        print('Введите число цифрами!')
Store_S = Scanner(2, num_scan)
Store.update(Store_S.out_scanner())
while True:
    num_xerox = input('Введите количество ксероксов, поступивших на склад: ')
    if num_xerox.isdigit():
        break
    else:
        print('Введите число цифрами!')
Store_X = Xerox(3, num_xerox)
Store.update(Store_X.out_xerox())

All_goods = Office(Store)
print("Количество товара поступило на склад:")
print(All_goods)

D = {}


for i in range(3):
    while True:
        num_key = input('Введите номер оргтехники для отгрузки со склада: 1 - принтер, 2 - сканер, 3 - ксерокс: ')
        if num_key.isdigit() and int(num_key) <= 3 and int(num_key) != 0:
            break
        else:
            print('Введите правильное число!')
    num_key = int(num_key)
    while True:
        num_par = input('Введите количество: ')
        if num_par.isdigit():
            break
        else:
            print('Введите число цифрами!')
    P = Printer(num_key, num_par)
    S = Scanner(num_key, num_par)
    X = Xerox(num_key, num_par)
    if num_key == 1:
        D.update(P.out_printer())
    elif num_key == 2:
        D.update(S.out_scanner())
    elif num_key == 3:
        D.update(X.out_xerox())
Sending = Office(D)
print("Количество товара для отправки:")
print(Sending)
