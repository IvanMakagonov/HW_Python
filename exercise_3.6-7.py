def int_func(a):
    a = list(map(lambda x: x.capitalize(), a.split(" ")))
    return " ".join(a)


a = "asd dsa sfa asdasffsa"
print(int_func(a))