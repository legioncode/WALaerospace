from code.classes.cargo import *
from code.classes.spacecraft import *
import numpy as np
import pandas as pd
from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.helperfunctions.possiblemoves import *
from code.helperfunctions.assign import assign
from code.helperfunctions.assign import returnLastParcel


def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)


main('data/CargoList1.csv', 'data/SpaceCraft1.csv')
