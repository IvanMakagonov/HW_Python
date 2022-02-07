def my_func(a, b, c):
    sum = a + b + c - min(a, b, c)
    return sum


print(f"Сумма двух самых больших элементов равна: {my_func(100, 20, 30)}")