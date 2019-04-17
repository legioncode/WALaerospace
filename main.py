from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.algoritmes.dhl import dhl
from code.algoritmes.ups import rnjesus, randomsolver
from code.algoritmes.postnl import postnl


def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    print(rnjesus(shiplist, parcellist))


main('data/CargoList1.csv', 'data/SpaceCraft1.csv')
