# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# 	Считаем 3 + 33 + 333 = 369.

number = int(input("Введите целое число: "))
if number < 0:
	S = str(- number)
	print("-%s - %s - %s =" % (S, S*2, S*3), (-(int(S) + int(S*2) + int(S*3))))
elif number >= 0:
	S = str(number)
	print("%s + %s + %s =" % (S, S*2, S*3), (int(S) + int(S*2) + int(S*3)))
