mijn_dict = {'vis' : 10, 'vlees' : 25, 'overig' : 15}

totaal = 50

def toon_inkomsten(inkomsten, totaal):
    for item, bedrag in inkomsten.items():
        print(f"{item}:{bedrag} euro")
        print("=========================")
        print(f"Totaal : {totaal} euro")
