#Входные данные
mas = [9, 7, 5, 5, 3, 1]
rating = input("Введите целое положительное число: ")

#Проверка на корректность введенных данных с помощью .isdigit()
while True:
    if rating.isdigit() == True and rating != "0":
        rating = int(rating)
        break
    else:
        rating = input("Вы ввели не целое число, введите целое положительное число: ")

#Распределение рейтинга
for i in range(len(mas)):
    if mas[i-1] >= rating and mas[i] <= rating or mas[0] < rating:
        mas.insert(i, rating)
        print(mas)
        break


