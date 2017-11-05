def tah(pole, cislo_policka, symbol):
    """Vrátíherní pole s daným symbolem umístěným na danou pozici"""
    novepole = pole[:cislo_policka] + symbol + pole[cislo_policka+1:]
    return novepole