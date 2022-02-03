chislo = int(input("Введите целое число: "))
chislo_1 = 0

while chislo != 0:
     if chislo_1 <= chislo % 10:
          chislo_1 = chislo % 10
     chislo //= 10

print(chislo_1)