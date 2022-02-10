from sys import argv

name, chas, stavka, cash = argv
try:
    print(int(chas)*int(stavka) + int(cash))
except:
    print("Вы ввели неправильные данные.")