class Cell:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return Cell(self.a + other.a)

    def __str__(self):
        return f"{self.a}"

    def __sub__(self, other):
        if self.a - other.a > 0:
            return Cell(self.a - other.a)
        else:
            return "Ошибка"

    def __mul__(self, other):
        return Cell(self.a * other.a)

    def __truediv__(self, other):
        return Cell(self.a / other.a)

    def make_order(self, strok):
        return "\n".join(["!" * strok for _ in range(self.a // strok)]) + "\n" + "@" * (self.a % strok)

c_1 = Cell(120)
c_2 = Cell(50)

print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_2.make_order(9))