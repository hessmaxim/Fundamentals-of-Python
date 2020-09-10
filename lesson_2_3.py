# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month = int(input())
list_month = ['зима', 'весна', 'лето', 'осень']
if month == 1 or month == 2 or month == 12:
    print(list_month[0])
elif month == 3 or month == 4 or month == 5:
    print(list_month[1])
elif month == 6 or month == 7 or month == 8:
    print(list_month[2])
elif month == 9 or month == 10 or month == 11:
    print(list_month[3])
else:
    print("Ошибка")

############################################################################################################

seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

month = int(input())
if month > 12 or month < 1:
    print("Ошибка")
else:
    for key in seasons.keys():
        if month in seasons[key]:
            print(key)

