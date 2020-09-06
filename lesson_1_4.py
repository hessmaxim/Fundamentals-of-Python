user_num = input('Введите целое положительное число: ')

i = 0
max_num = int(user_num[i])

while i < len(user_num)-1:
    if max_num < int(user_num[i+1]):
        max_num = int(user_num[i+1])
    i += 1
print(max_num)

