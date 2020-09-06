number = int(input("Введите целое число: "))
if number < 0:
	S = str(- number)
	print("-%s - %s - %s =" % (S, S*2, S*3), (-(int(S) + int(S*2) + int(S*3))))
elif number >= 0:
	S = str(number)
	print("%s + %s + %s =" % (S, S*2, S*3), (int(S) + int(S*2) + int(S*3)))