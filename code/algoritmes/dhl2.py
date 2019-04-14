from code.classes.cargo import *
from code.classes.spacecraft import *
import numpy as np
import pandas as pd
from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.helperfunctions.possiblemoves import *
from code.helperfunctions.assign import assign
from code.helperfunctions.assign import returnLastParcel


def dhl2(shiplist, parcellist):

    finallist = []
    for c in parcellist:
        shipmw = [x.mw for x in shiplist]
        while True:
            defaultship = (0, 400)

            for z in range(len(shipmw)):
                difference = max(shipmw[z], i.mw) - min(shipmw[z], i.mw)
                if difference < defaultship[1]:
                    defaultship = (z, difference)

            if checkmove(i, shiplist[defaultship[0]]):
                assign(shiplist[defaultship[0]], i)
                break
            else:
                shipmw.pop(defaultship[0])
            if len(shipmw) == 0:
                finallist.append(i)
                break


    for y in shiplist:
        print('ship' + str(y.name) + str(len(y.assigned)) + '    ' + str(y.payload) + ' ' + str(y.volume))
    print('--------------------------------------------')
    print('finallistlength:' + str(len(finallist)))
    print(shiplist[0].mw)
