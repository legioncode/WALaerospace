from code.classes.cargo import *
from code.classes.spacecraft import *
import numpy as np
import pandas as pd
from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.helperfunctions.possiblemoves import *
from code.helperfunctions.assign import assign
from code.helperfunctions.assign import returnLastParcel
from code.algoritmes.heekstra import heekstra


def dhl(shiplist, parcellist):
    extralist = []
    for i in parcellist:
        shipmw = [x.mw for x in shiplist]
        defaultship = (0,400)

        for z in range(len(shipmw)):
            difference = max(shipmw[z], i.mw) - min(shipmw[z], i.mw)
            if difference < defaultship[1]:
                defaultship = (z, difference)

        if checkmove(i, shiplist[defaultship[0]]):
            assign(shiplist[defaultship[0]], i)
        else:
            extralist.append(i)


    for y in shiplist:
        print('ship' + str(y.name) + str(y.assigned))
    print('--------------------------------------------')
    print(possiblemovesA(shiplist, extralist))
