from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.algoritmes.dhl import dhl
from code.algoritmes.ups import ups
from code.algoritmes.postnl import postnl
from code.algoritmes.chinapost import chinapost

def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    ups(shiplist, parcellist)


main('data/CargoList1.csv', 'data/SpaceCraft1.csv')
