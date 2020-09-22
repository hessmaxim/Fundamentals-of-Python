"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

"""

my_file = open("text_3.txt", encoding="utf-8")
condition = 20000
av_salary = 0
count_str = 0

for line in my_file:
    count_str += 1
    s = line.split()
    av_salary = (av_salary + float(s[1]))
    if float(s[1]) < condition:
        print(s[0])

my_file.close()

av_salary /= count_str
print(f"\nСредняя величина дохода сотрудников = {av_salary: .2f}")
