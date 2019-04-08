from data.cargo import *
import numpy as np
import pandas as pd
from code.helperfunctions.readers import cargoreader
from code.helperfunctions.readers import shipreader

<<<<<<< HEAD
def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    for i in parcellist:
        print(i.mw)
=======
def main():
    cargodict = cargoreader('CargoList1.csv')
    shipdict = shipreader('SpaceCraft1.csv')
    print(cargodict)
    #print(shipdict)
>>>>>>> 27e55572e21a70e17bb258a8264733447f0b9837

main('CargoList1.csv', 'SpaceCraft1.csv')
