from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f'''Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro.'''
    return uitvoer

print(aanbieding_1("aardbei",4,0.1))



inkomsten_per_dag = [220,430,125,160,205,90,345]
btw = 0.09

def inkomsten_totaal(inkomsten):
    totaal = 0
    for inkomsten in inkomsten_per_dag:
        totaal += inkomsten
    bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return uitvoer

print(inkomsten_totaal(inkomsten_per_dag))



mijn_lijst = [220,430,125,160,205,90,345]

def laag_en_hoog(mijn_lijst):
    laag = min(mijn_lijst)
    hoog = max(mijn_lijst)
    uitvoer = [laag,hoog]
    return uitvoer

print(laag_en_hoog(mijn_lijst))


def gemiddelde(mijn_lijst):
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    return uitvoer

print(gemiddelde(mijn_lijst))



invoer_lijst = [10,5,3,2,1,2,9]

def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer

print(meervoudig(invoer_lijst))



def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer