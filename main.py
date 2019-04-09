from code.classes.cargo import *
from code.classes.spacecraft import *
import numpy as np
import pandas as pd
from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.helperfunctions.possiblemoves import *

def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    workcraft = shiplist[0]
    print([i.name for i in shiplist])
    print(possiblemovesA(shiplist, parcellist))
    #print(possiblemovesB(shiplist, parcellist))
    #print(possiblemovesC(shiplist, parcellist))
main('data/CargoList1.csv', 'data/SpaceCraft1.csv')
