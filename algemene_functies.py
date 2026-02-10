def mijn_functie_1(argument):
    teruggeefwaarde = argument ** 2
    return teruggeefwaarde

print(mijn_functie_1(4))

def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a//b)
    return uitvoer_lijst

print(mijn_functie_2(12,3))