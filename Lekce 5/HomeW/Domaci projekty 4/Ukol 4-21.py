for cislo in range(1,101):
    if cislo % 3 == 0 and cislo % 5 == 0:
        print("bum-bác")
    elif cislo % 3 == 0:
        print("bum")
    elif cislo % 5 == 0:
        print("bác")
    else:
        print(cislo)