def fact(a):
    for i in range(1, a):
        yield i

b = 1
for i in fact(10):
    b *= i
    print(f"{i}! = {b}")