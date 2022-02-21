import random

class Car:
    def __init__(self, color, name, is_police = False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        while True:
            try:
                self.speed = int(input("Введите вашу скорость (целое натуральное число): "))
                print(f"Cкорость {self.name} {self.speed} км/ч.")
                break
            except:
                print("Вы ввели некоректные данные, введите заного.")
        return self.speed

    def stop(self):
        self.speed = 0
        print(f"{self.name} остановилась.")
        return self.speed

    def turn_pls(self):
        self.turn = random.randrange(0, 2)
        if self.turn == 0:
            print(f"{self.name} повернула налево")
        elif self.turn == 1:
            print(f"{self.name} едет прямо")
        else:
            print(f"{self.name} повернула направо")

    def show_speed(self):
        if self.speed >= 80 and self.is_police == False:
            print(f"Скорость машины {self.name} ограничена в 80 км/ч! Сбавьте скорость!")
        else:
            print(f"{self.name} едете правильно! Ваша скорость {self.speed} км/ч")

class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print("Скорость в городе не более 60 км/ч! Сбавьте скорость!")
        else:
            print(f"{self.name} едете правильно! Ваша скорость {self.speed} км/ч")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40 and self.is_police == False:
            print(f"{self.name} может ехать не более 40 км/ч! Сбавьте скорость!")
        else:
            print(f"{self.name} едете правильно! Ваша скорость {self.speed} км/ч")

class PoliceCar(Car):
    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True

a = WorkCar("Blue", "BMW")
b = PoliceCar("White", 'Lada')
c = SportCar("Red", "Lamba")
d = TownCar("White", "RR")

mas = [a, b, c, d]

for i in mas:
    i.go()
    i.turn_pls()
    i.turn_pls()
    i.show_speed()
    i.turn_pls()
    i.stop()