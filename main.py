from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.algoritmes.dhl import dhl
from code.algoritmes.ups import randomsolver
from code.algoritmes.postnl import postnl
from code.algoritmes.chinapost import chinapost

def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    #randomsolver(shiplist, parcellist)
    #postnl(shiplist, parcellist)
    chinapost(shiplist, parcellist)


main('data/CargoList1.csv', 'data/SpaceCraft1.csv')
