def func(a, b):
    try:
        print(f"{a} / {b} = {int(a) / int (b)}")
    except:
        print("Вы ввели некоректные данные")


func(input("Введите число a: "), input("Введите число b: "))