from cargo import *
import numpy as np
import pandas as pd
from readers import *
from spacecraft import *

def main(cargocsv, shipcsv):
    parcellist = loadparcels(cargocsv)
    shiplist = loadships(shipcsv)
    for i in parcellist:
        print(i.mw)

main('CargoList1.csv', 'SpaceCraft1.csv')
