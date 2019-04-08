from code.classes.cargo import *
import numpy as np
import pandas as pd
from code.helperfunctions.readers import cargoreader
from code.helperfunctions.readers import shipreader


def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    print(parcellist)
    print()
    print()
    print(shiplist)

main('CargoList1.csv', 'SpaceCraft1.csv')
