import numpy as np
import pandas as pd
import random
from code.algoritmes.dhl import dhl, dhlonsteroids
from code.helperfunctions.possiblemoves import checkmove, possiblemovecost
from code.helperfunctions.assign import assign, loadstate, clearships


# def popspacecraft():

def maersk(shiplist, parcellist):
    #possiblelist = possiblemovecost(shiplist, parcellist)
    # while possiblelist != []:
    hoi = dhl(shiplist, parcellist)
    clearships(shiplist)
    for i in shiplist:
        print(i.assigned)
    loadstate(hoi, shiplist)
    for i in shiplist:
        print(i.assigned)
