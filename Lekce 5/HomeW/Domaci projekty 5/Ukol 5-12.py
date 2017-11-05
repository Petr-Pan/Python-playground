def tah_pocitace(pole):
    """Vrátí herní pole se zaznamenaným tahem počítače."""
    from random import randrange
    while True:
        cislo_policka = randrange(0,20)
        if "-" in pole[cislo_policka]:
            break
        else:
            continue
    novepole = pole[:cislo_policka] + symbol + pole[cislo_policka+1:]
    return novepole