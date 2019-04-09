from code.classes.cargo import *
from code.classes.spacecraft import *
from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.helperfunctions.possiblemoves import *
from code.helperfunctions.assign import assign
from code.helperfunctions.assign import returnLastParcel
from code.algoritmes.heekstra import heekstra
from code.algoritmes.dhl    import dhl

def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    dhl(shiplist, parcellist)


main('data/CargoList1.csv', 'data/SpaceCraft1.csv')
