new = open("text_5.txt", "w+", encoding = "utf-8")

new.write(input("Введите цифры через пробел: "))
new.seek(0)
#mas = new.readline().split(" ")
#mas = [float(mas[i]) for i in range(len(mas))]

print(f"Сумма чисел = {sum(map(int, new.readline().split(' ')))}")