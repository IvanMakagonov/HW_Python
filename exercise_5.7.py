import json
new = open("text_7.txt", "r", encoding="utf-8")

new_dict = {}
for i in new.readlines():
    mas = i.split(' ')
    mas = [mas[0] + " " + mas[1]] + [int(mas[2]) - int(mas[3])]
    if mas[1] >= 0:
        new_dict[mas[0]] = mas[1]

mas_1 = [new_dict, {"sredniya_pribl": sum(new_dict.values())}]
print(mas_1)
with open("my_file.json", "w") as text_777777:
    json.dump(mas_1, text_777777)

