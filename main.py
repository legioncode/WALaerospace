from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.algoritmes.dhl import dhl, dhlonsteroids
from code.algoritmes.ups import ups
from code.algoritmes.postnl import postnl
from code.algoritmes.depth import depth
from code.algoritmes.flessenpost import flessenpost
import math
from code.helperfunctions.cargototals import totals


def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    #ups(shiplist, parcellist)
    #depth(shiplist, parcellist)
    #postnl(shiplist, parcellist)
    #flessenpost(shiplist, parcellist)
    #dhlonsteroids(shiplist, parcellist)
    #totals(parcellist, shiplist)


main('data/CargoList2.csv', 'data/SpaceCraft1.csv')
