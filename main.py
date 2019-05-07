from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
#from code.algoritmes.dhl import dhl, dhlonsteroids
#from code.algoritmes.ups import ups
#from code.algoritmes.postnl import postnl
#from code.algoritmes.depth import depth
from code.algoritmes.flessenpost import flessenpost
from code.helperfunctions.visualization import visual
import math
#from code.helperfunctions.cargototals import totals
#from code.algoritmes.breadth import Breadth
#from code.algoritmes.beam import Beam
#from code.algoritmes.maersk import *
#from code.algoritmes.breadth2 import Breadth2


def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    # ups(shiplist, parcellist)
    # depth(shiplist, parcellist)
    # postnl(shiplist, parcellist)
    visual(flessenpost(shiplist, parcellist))
    # dhlonsteroids(shiplist, parcellist)
    # totals(parcellist, shiplist)
    #Breadth(shiplist, parcellist)
    #Beam(shiplist, parcellist)
    #Breadth2(shiplist, parcellist)
    #maersk(shiplist, parcellist)


main('data/CargoList1.csv', 'data/SpaceCraft1.csv')
