import time
class TrafficLight:
    #атрибуты
    __color = ""

    #методы класса
    def running(self):
        while True:
            print("Цвет красный")
            time.sleep(7)
            print(f"Цвет желтый")
            time.sleep(3)
            print(f"Цвет зеленый")
            time.sleep(10)
            print('Цвет желтый')
            time.sleep(3)


a = TrafficLight()
a.running()


