mijn_dict = {'vis' : 10, 'vlees' : 25, 'overig' : 15}

totaal = 50

def presenteer(mijn_dict,totaal):
    for key,value  in mijn_dict.items(): 
        print(f"{key} : {value} euro")
    print("=" * 26)
    print(f"totaal : {totaal} euro")


presenteer(mijn_dict,totaal)
    
# vraag 8 