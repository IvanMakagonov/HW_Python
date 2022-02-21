class Road:
    #атрибуты
    def __init__(self, length, width):
        self._length = length
        self._width = width
    #методы
    def raschet(self, mas = 25, vis = 5):
        print(f"{self._length} м * {self._width} м * {mas} кг * {vis} см = {self._length * self._width * mas * vis} кг")

Road(100, 10).raschet()