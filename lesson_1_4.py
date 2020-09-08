# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    user_num = input('Введите целое положительное число: ')
    if int(user_num) >= 0:
        break

i = 0
max_num = int(user_num[i])

while i < len(user_num)-1:
    if max_num < int(user_num[i+1]):
        max_num = int(user_num[i+1])
    i += 1
print(max_num)

