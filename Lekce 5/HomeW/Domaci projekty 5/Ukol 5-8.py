from random import randrange
#Dalo by se nějak snáz provést vyhodnocení vítěze?
P1pocethodu = int(0)
P2pocethodu = int(0)
P3pocethodu = int(0)
P4pocethodu = int(0)

P1hody=int(0)
P2hody=int(0)
P3hody=int(0)
P4hody=int(0)

while P1hody != 6:
    P1hody = randrange(1,7)
    print("Hráč 1 hodil", P1hody,"!")
    P1pocethodu +=1

while P2hody != 6:
    P2hody = randrange(1,7)
    print("Hráč 2 hodil", P2hody,"!")
    P2pocethodu += 1

while P3hody != 6:
    P3hody = randrange(1,7)
    print("Hráč 3 hodil", P3hody,"!")
    P3pocethodu += 1

while P4hody != 6:
    P4hody = randrange(1,7)
    print("Hráč 4 hodil", P4hody,"!")
    P4pocethodu += 1

viteznychhodu=max(P1pocethodu, P2pocethodu, P3pocethodu, P4pocethodu)

print()

if P1pocethodu >= P2pocethodu and P1pocethodu >= P3pocethodu and P1pocethodu >= P4pocethodu:
    print("Vítězí hráč 1 s", viteznychhodu, "body!")
elif P2pocethodu >= P1pocethodu and P2pocethodu >= P3pocethodu and P2pocethodu >= P4pocethodu:
    print("Vítězí hráč 2 s", viteznychhodu, "body!")
elif P3pocethodu >= P1pocethodu and P3pocethodu >= P2pocethodu and P3pocethodu >= P4pocethodu:
    print("Vítězí hráč 3 s", viteznychhodu, "body!")
elif P4pocethodu >= P1pocethodu and P4pocethodu >= P2pocethodu and P4pocethodu >= P3pocethodu:
    print("Vítězí hráč 4 s", viteznychhodu, "body!")
else:
    print("Někde je chyba a zajímá mě to.")
