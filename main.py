from code.classes.cargo import *
from code.classes.spacecraft import *
from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.helperfunctions.possiblemoves import *
from code.helperfunctions.assign import assign
from code.helperfunctions.assign import returnLastParcel
from code.algoritmes.dhl    import dhl
from code.algoritmes.postnl import postnl

def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    postnl(shiplist, parcellist)

main('data/CargoList1.csv', 'data/SpaceCraft1.csv')
