revenue = int(input("Введи выручку компании: "))
costs = int(input("Введите издержки компании: "))

if revenue > costs:
    print(f"Ваше преприятие работает в плюс {revenue - costs} рублей!")
elif revenue < costs:
    print(f"Ваше предприятие работает в минус {costs - revenue} рублей!")
else:
    print("Ваша компания работает в 0 рублей!")