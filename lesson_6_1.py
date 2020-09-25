"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.

"""

import time


class TrafficLight:

    __color = ['RED', 'YELLOW', 'GREEN']

    second = 1

    def run_red(self):
        t_r = 7
        r = f"\033[31m {self.__color[0]}"

        for i in range(t_r):
            print(r, end='')
            time.sleep(self.second)
        print()

    def run_yellow(self):
        t_y = 2
        y = f"\033[33m {self.__color[1]}"

        for i in range(t_y):
            print(y, end='')
            time.sleep(self.second)
        print()

    def run_green(self):
        t_g = 7
        g = f"\033[32m {self.__color[2]}"

        for i in range(t_g):
            print(g, end='')
            time.sleep(self.second)
        print()

    def running(self, timing):

        for i in range(timing):
            self.run_red()
            self.run_yellow()
            self.run_green()
            self.run_yellow()


user_enter = input('Start the Traffic Light program (y/n)? ')
if user_enter == 'y':
    run = TrafficLight()
    time_program = int(input('How many cycles should the program run (1 cycle - 18 s): '))
    run.running(time_program)
else:
    print('Program launch canceled by user.')


