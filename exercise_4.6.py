import itertools as it

def fun_2(a, b):
    for i in it.count(a):
        if i <= b:
            print(i)
        else:
            print("_" * 30)
            break


def fun_1(a, c, b = 0):
    for i in it.cycle(a):
        if b > c:
            print("_" * 30)
            break
        else:
            print(i)
            b += 1


fun_1([1, 2, 3], 15)
fun_2(10, 25)