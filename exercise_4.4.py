import random

mas= [random.randint(0, 20) for x in range(1, 30)]
print(mas)
my_dict = {x: x for x in mas}
print(my_dict.keys())