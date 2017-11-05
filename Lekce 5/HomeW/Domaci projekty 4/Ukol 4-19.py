a = int(input("Zadej první číslo: "))
b = int(input("Druhé: "))
c = int(input("Třetí: "))

if a + b + c > 10:
    print("Součet je větší než deset.")
elif a + b + c <= 10:
    print("Součet je menší nebo roven deseti.")
else:
    print("Záhadná, nepokrytá chyba.")