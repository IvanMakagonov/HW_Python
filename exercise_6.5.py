class Stationery:
    def __init__(self):
        self.title = "Мы"

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"{self.title} работаем с ручкой.")

class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} работаем с карандашом.")

class Handle(Stationery):
    def draw(self):
        print(f"{self.title} работаем с маркером")

Stationery().draw()
Pen().draw()
Pencil().draw()
Handle().draw()