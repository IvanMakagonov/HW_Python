def my_func(x, y):
    step = x
    for i in range(abs(y) - 1):
        step = step * x
    step = 1 / step
    return step

print(my_func(10.8, -2))
