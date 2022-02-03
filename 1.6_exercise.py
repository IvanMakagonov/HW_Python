revenue = int(input("Введи выручку компании: "))
costs = int(input("Введите издержки компании: "))

if revenue > costs:
    print(f"Ваше преприятие работает в плюс {revenue - costs} рублей!")
    profit = revenue - costs
    print(f"Рентабельность выручки: {profit / revenue * 100:.2f} %!") 
    workers = int(input("Введите количество сотрудников: "))
    print(f"Прибыль фирмы в расчёте на одного сотрудника: {profit / workers:.2f} рублей")
elif revenue < costs:
    print(f"Ваше предприятие работает в минус {costs - revenue} рублей!")
else:
    print("Ваша компания работает в 0 рублей!")