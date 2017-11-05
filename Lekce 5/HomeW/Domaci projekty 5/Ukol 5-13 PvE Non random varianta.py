#Problém s ošetřením vstupu hráče, aby byl 0-19. Když nedám "cislo_policka = int(input("Zadej pozici (0-19): "))" nejde mi na následujícím řádku použít např. "if cislo_policka >= 0".
#Když to tak nechám, program celkem smysluplně crashuje při zadání čehokoliv nečíselného.

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

def tah_hrace(pole):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici.
    Pozici udává hráč."""
    while True:
        cislo_policka = int(0)
        cislo_policka = int(input("Zadej pozici (0-19): "))
        if cislo_policka >= 0 and cislo_policka <= 19 and "x" not in pole[cislo_policka] and "o" not in pole[cislo_policka]:
            break
        elif cislo_policka < 0 or cislo_policka >19:
            print("Chyba. Zadej číslo od 0 do 19.")
        elif "x" in pole[cislo_policka] or "o" in pole[cislo_policka]:
            print("Pozice obsazena. Již je zde: ", pole[cislo_policka], ".")
        else:
            print("Chyba. Naprosto neznámého typu. Gratuluji.")
            
    symbol = "x"
    novepole = pole[:cislo_policka] + symbol + pole[cislo_policka+1:]
    return novepole

def tah_pocitace(pole):
    """Vrátí herní pole se zaznamenaným tahem počítače."""
    from random import randrange
    while True:
        cislo_policka = int(21)
        
        if "o" in pole:
            nahoda = randrange(0,2)
            if nahoda == 0:
                nahoda = -1
            cislo_policka = int(pole.index("o") + nahoda)
            while "-" not in pole[cislo_policka]:
                if "x" in pole[cislo_policka] or "o" in pole[cislo_policka]:
                    cislo_policka += 1
                    if cislo_policka > 19:
                        cislo_policka = 0
            break
        else:
            cislo_policka = int(randrange(0,20))
            
            if "-" in pole[cislo_policka]:
                break
        
    symbol = "o"
    novepole = pole[:cislo_policka] + symbol + pole[cislo_policka+1:]
    return novepole

def piskvorky1d():
    """Spustí celou hru piskvorky střídavým voláním funkcí."""
    pole = "--------------------"
    print(pole)
    
    while vyhodnot(pole) == "-":
        pole = (tah_hrace(pole))
        print(pole)
        if vyhodnot(pole) == "x" or vyhodnot(pole) == "o" or vyhodnot(pole) == "!":
            break
        pole = (tah_pocitace(pole))
        print(pole)
        
    if vyhodnot(pole) == "x":
        print("Gratuluji! Vyhráls!")
    elif vyhodnot(pole) == "o":
        print("Negratuluji. Nevyhráls.")
    elif vyhodnot(pole) == "!":
        print("Téměř gratuluji. Remizovals.")

piskvorky1d()
