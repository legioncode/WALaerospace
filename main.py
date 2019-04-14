from code.classes.cargo import *
from code.classes.spacecraft import *
from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from possiblemoves import *

def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    workcraft = shiplist[0]
    print([i.name for i in shiplist])
    #print(possiblemovesA(shiplist, parcellist))
    #print(possiblemovesB(shiplist, parcellist))
    #print(possiblemovesC(shiplist, parcellist))
main('data/CargoList1.csv', 'data/SpaceCraft1.csv')
