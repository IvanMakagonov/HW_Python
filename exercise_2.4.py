text = input("Введите несколько слов через пробелом: ")
text = text.split(" ")

#Удаляет пустые элементы списка
for i in range(text.count('')):
    text.remove('')

#Пишем слова
for i in range(len(text)):
    print(f"{i + 1}) {text[i][0:10]}")