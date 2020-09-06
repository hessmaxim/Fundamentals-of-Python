proceeds = int(input('Введите значение выручки: '))
cost = int(input('Введите значение издержек: '))

profit = proceeds - cost
prof_pro = profit * 100 / proceeds

if profit > 0:
    print('Ваша прибыль составила %d условных единиц или %d %%.' % (profit, prof_pro))
    num = int(input('Сколько сотрудников в вашей фирме?'))
    print('Каждый сотрудник приносит прибыль в размере %f условных единиц' % (profit / num))
elif profit < 0:
    print('Ваша фирма приносит убытки в размере %d условных единиц или %d %%.' % (profit, prof_pro))
else:
    print('Ваша прибыль составила 0 %.')
