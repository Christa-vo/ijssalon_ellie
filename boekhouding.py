from helper import *
from presentatie import *

inkomsten = {
    "Aardbeien-ijs-totaal" : int("1000"),
    "Vanille-ijs-totaal" : int("2000"),
    "Chocolade-ijs-totaal" : int("1500"),
    "Waterijsjes-totaal" : int("750"),
}

totaal_inkomsten = som(inkomsten)

presenteer(inkomsten,totaal_inkomsten)