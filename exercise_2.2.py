mas = input("Введите данные для масива через пробел:").split(" ")

#Удаляет пустые элементы списка
for i in range(mas.count('')):
    mas.remove('')

#Меняем местами соседние элементы
for i in range(len(mas)):
    if i == 0 or i % 2 == 0:
        mas.insert(i + 2, mas[i])
        mas.pop(i)

print(mas)