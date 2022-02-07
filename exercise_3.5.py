test = 1
def func(a):
    global globa, test
    mas_1 = a.split(" ")
    globa = 0
    for i in range(len(mas_1)):
        if mas_1[i] != 'exit':
            globa += int(mas_1[i])
        else:
            test = 0
            return globa
    return globa


while test == 1:
    try:
        print(f"Результат: {func(str(globa)+ ' ' + input('Добавтьте ещё чисел, для выхода введите exit: '))}")
    except:
        print(f"Результат: {func(input('Введите числа для сложения через пробел: '))}")
