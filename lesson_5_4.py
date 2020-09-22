"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""

template = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

my_file = open("text_4.txt", encoding="utf-8")
new_my_file = open("text_41.txt", "w", encoding="utf-8")

for line in my_file:
    s = line.split()
    if s[0] in template:
        temp = line.replace(s[0], template[s[0]])
        new_my_file.write(temp)

my_file.close()
new_my_file.close()
