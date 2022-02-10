import random

mas= [random.randint(0, 1000) for x in range(1, 30)]
print(mas)
otvet = [mas[x] for x in range(1, len(mas)) if mas[x] > mas[x-1]]
print(otvet)