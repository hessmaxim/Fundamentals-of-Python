S = "Задание 1"
print(S, "\n\nЗдравствуйте!")
name = input("Введите ваше имя: ")
yearOfBirth = int(input("Введите год рождения:"))
year = 2020
age = year - yearOfBirth
print("%s, вам %d года/лет." % (name, age))

print("\n\nАрифметика:\n")
x = 100
y = 36
print("%d + %d =" % (x, y), x + y)
print("%d - %d =" % (x, y), x - y)
print("%d / %d =" % (x, y), "%.0f" % (x / y))
print("%d // %d =" % (x, y), x // y)
print("%d %% %d =" % (x, y), x % y)
