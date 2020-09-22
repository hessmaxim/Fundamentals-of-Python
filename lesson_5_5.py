"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""

my_file = open("text5.txt", "w", encoding="utf-8")

s = input('Введите числа через пробел: ')
my_file.write(s)

my_file = open("text5.txt", encoding="utf-8")

for line in my_file:
    s = line.split()

sum_num = 0
for el in s:
    sum_num += int(el)
print(sum_num)

my_file.close()
