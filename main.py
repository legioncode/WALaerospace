from data.cargo import *
import numpy as np
import pandas as pd
from code.helperfunctions.readers import cargoreader
from code.helperfunctions.readers import shipreader

def main():
    cargodict = cargoreader('CargoList1.csv')
    shipdict = shipreader('SpaceCraft1.csv')
    print(cargodict)
    #print(shipdict)

main()
