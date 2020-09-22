"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.

"""

my_file = open("text1.txt", encoding="utf-8")
count_str = 0

for line in my_file:
    count_str += 1
    s = line.split()
    print(f"Количество слов в {count_str} строке - {len(s)}")
    print(f" {count_str} строка:     {line}")

my_file.close()
print(f"Всего строк в файле: {count_str}")
