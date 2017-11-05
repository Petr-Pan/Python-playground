#Nefunkční. TypeError: unsupported operand type(s) for +=: 'type' and 'int'

n = int(input("Zadej číslo: "))
vysledek = int
for k in range(0,n+1):
    mezivysledek = n*k
    vysledek += mezivysledek
#n*(n-1)
print(vysledek)
