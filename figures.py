import math  

print("Избери фигура:")
print("1 - Кръг")
print("2 - Квадрат")
print("3 - Правоъгълник")
print("4 - Триъгълник")

choice = input("Въведи номер: ")

if choice == "1":
    r = float(input("Въведи радиус: "))
    area = math.pi * r**2

elif choice == "2":
    a = float(input("Въведи страна: "))
    area = a**2

elif choice == "3":
    a = float(input("Въведи страна a: "))
    b = float(input("Въведи страна b: "))
    area = a * b

elif choice == "4":
    a = float(input("Въведи основа: "))
    h = float(input("Въведи височина: "))
    area = (a * h) / 2

else:
    area = None
    print("Невалиден избор!")

if area is not None:
    print("Лицето е:", area)