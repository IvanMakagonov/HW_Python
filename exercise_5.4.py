new = open("text_4.txt", "r", encoding = "utf-8")
new_1 = open("text_4.1.txt", "w", encoding="utf-8")

for i in new.readlines():
    mas = i.split(' ')
    if mas[0] == "One":
        mas[0] = "Один"
    elif mas[0] == 'Two':
        mas[0] = "Два"
    elif mas[0] == 'Three':
        mas[0] = "Три"
    elif mas[0] == 'Four':
        mas[0] = "Четыре"
    new_1.write(f"{mas[0]} {mas[1]} {mas[2]}")