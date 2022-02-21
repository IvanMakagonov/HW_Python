class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {1: wage, 2: bonus}

class Position(Worker):
    def get_full_name(self):
        print(f"Работник: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Зарплата {self.position} = {self._income.get(1) + self._income.get(2)} рублей")

Position("Ivan", "Ivanov", "Director", 10000, 200).get_full_name()
Position("Ivan", "Ivanov", "Director", 10000, 200).get_total_income()

Position("Sergei", "Hazernik", "Cleaner", 100000, 2000).get_full_name()
Position("Sergei", "Hazernik", "Cleaner", 100000, 2000).get_total_income()


