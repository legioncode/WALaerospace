from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import possiblemovesA
from code.helperfunctions.assign import assign, calculatepackages, returnLastParcel, solution, undomove


def tester(shiplist, cargolist):
    sol = (0, {})
    children = possiblemovesA(shiplist, cargolist)
    movelist = []
    nParcels = len(cargolist)
