mas = []
chislo = 1

while True:
    print("1) Введите '1' если хотите добавить данные.\n2) Введите '2' если хотите посмотреть аналитику.\n"
          "3) Введите '3' если хотите удалить данные\n4) Введите '4' если вы хотите выйти")
    vibor = input("Введите свой выбор: ")
    if vibor == "1":
        a = input("Название:")
        b = input("Цена:")
        c = input("Количество:")
        d = input("Ед:")
        kort = (chislo, {'название' : a, 'цена' : b, 'количество' : c, 'ед.' : d})
        mas.append(kort)
        chislo += 1
        print(mas)
    elif vibor == "3":
        for i in range(len(mas)):
            print(f"{mas[i][0]}-id:\nНазвание: {mas[i][1].get('название')}\nЦена: {mas[i][1].get('цена')}\n"
                  f"Количество: {mas[i][1].get('количество')}\nЕд.: {mas[i][1].get('ед.')}\n{30 * '_'}")
        delite = int(input("Введите номер позицию, которую хотите удалить целым числом: "))
        for i in mas:
            if i[0] == delite:
                mas.remove(i)
                print(f"Позиция товара с id {delite} удалена!\n{30 * '_'}")
    elif vibor == "2":
        print(f"{30*'_'}\nАналитика по товарам:\nID: {[i[0] for i in mas]}\nНазвание:{[i[1].get('название') for i in mas]}\nЦена:{[i[1].get('цена') for i in mas]}\n"
              f"Количество:{[i[1].get('количество') for i in mas]}\nЕд.:{[i[1].get('ед.') for i in mas]}\n{30*'_'}")
    elif vibor == "4":
        break