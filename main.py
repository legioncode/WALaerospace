from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
#from code.algoritmes.dhl import dhl, dhlonsteroids
from code.algoritmes.ups import ups, randomsolver
#from code.algoritmes.postnl import postnl
#from code.algoritmes.depth import depth
<<<<<<< HEAD
from code.algoritmes.flessenpost import flessenpost
from code.helperfunctions.visualization import visualpackages, massvolumeperc, randomplot
=======
#from code.algoritmes.flessenpost import flessenpost
#from code.helperfunctions.visualization import visualpackages, massvolumeperc
>>>>>>> 34eea1626be6a462bd705efae2abc8ee1e01c56b
import math
#from code.helperfunctions.cargototals import totals
from code.algoritmes.breadth import Breadth
#from code.algoritmes.beam import Beam
#from code.algoritmes.maersk import *
#from code.algoritmes.breadth2 import Breadth2


def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    print(ups(shiplist, parcellist))
    # depth(shiplist, parcellist)
    # postnl(shiplist, parcellist)
<<<<<<< HEAD
    # massvolumeperc(flessenpost(shiplist, parcellist))
    # dhlonsteroids(shiplist, parcellist)
    # totals(parcellist, shiplist)
    # Breadth(shiplist, parcellist)
    # Beam(shiplist, parcellist)
    # Breadth2(shiplist, parcellist)
    # maersk(shiplist, parcellist)
    # randomplot(shiplist, parcellist)
=======
    #massvolumeperc(flessenpost(shiplist, parcellist))
    # dhlonsteroids(shiplist, parcellist)
    # totals(parcellist, shiplist)
    Breadth(shiplist, parcellist)
    #Beam(shiplist, parcellist)
    #Breadth2(shiplist, parcellist)
    #maersk(shiplist, parcellist)
>>>>>>> 34eea1626be6a462bd705efae2abc8ee1e01c56b


main('data/CargoListSmall.csv', 'data/SpaceCraft1.csv')
