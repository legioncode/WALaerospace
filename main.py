from code.classes.cargo import *
import numpy as np
import pandas as pd
from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships


def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    workcraft = shiplist[0]
    print([i.name for i in shiplist])
main('data/CargoList1.csv', 'data/SpaceCraft1.csv')
