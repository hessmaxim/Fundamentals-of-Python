def div(var_1, var_2):
	""" Возвращает частное от деления.
	
	Позиционные аргументы:
		var_1 и var_2 - 
	числа, которые запрашиваются
	у пользователя.
	
	"""
	try:
		return var_1 / var_2
	except ZeroDivisionError:
		return "divisor not equal to 0:"


dividend = float(input('Enter the dividend number: '))
divisor = float(input('Enter divisor not equal to 0: '))
# while divisor == 0:
# 	divisor = float(input('Enter divisor not equal to 0: '))

print(f"Division result: {div(dividend, divisor)}")
