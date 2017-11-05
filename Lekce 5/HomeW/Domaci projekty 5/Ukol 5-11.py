def tah_hrace(pole):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici.
    Pozici udává hráč."""
    while True:
        cislo_policka = input("Zadej pozici (0-19): ")
        if cislo_policka >= 0 and cislo_policka <= 19 and pole[cislo_policka] != "x" and pole[cislo_policka] !="o":
            break
        elif pole[cislo_policka] == "x" or pole[cislo_policka] == "o":
            print("Pozice obsazena. Již je zde: ", pole[cislo_policka], ".")
        else:
            print("Chyba. Zadej číslo od 0-19.")
    
    novepole = pole[:cislo_policka] + symbol + pole[cislo_policka+1:]
    return novepole