# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("Выработка: ", first_param)
print("Ставка: ", second_param)
print("Премия: ", third_param)

salary = float(first_param) * float(second_param) + float(third_param)
print(f"Зарплата: {salary: .2f}")
