from cargo import *
import numpy as np
import pandas as pd
from readers import cargoreader
from readers import shipreader

def main():
    cargodict = cargoreader('CargoList1.csv')
    shipdict = shipreader('SpaceCraft1.csv')
    print(cargodict)
    print(shipdict)

main()
