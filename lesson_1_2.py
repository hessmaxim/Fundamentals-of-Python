user = int(input("Введите время в секундах: "))
second = user % 60
minute = int(user * 60 / 3600) % 60
hour = int(user / 3600)
print('{0:02}:{1:02}:{2:02}'.format(hour, minute, second))
