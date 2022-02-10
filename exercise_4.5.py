from functools import reduce

def func(a, b):
    return a * b

mas = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(func, mas))