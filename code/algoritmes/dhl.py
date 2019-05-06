import random
from code.helperfunctions.assign import assign, solution, returnLastParcel,  calculatetotal
from code.helperfunctions.possiblemoves import *
from code.helperfunctions.readers import loadships
from code.helperfunctions.readers import loadparcels
import pandas as pd
import numpy as np
from code.classes.spacecraft import *
sfrom code.classes.cargo import *


def dhl(shiplist, parcellist):
    extralist = []
    for i in parcellist:
        shipmv = [x.mv for x in shiplist]
        defaultship = (0, 400)

        for z in range(len(shipmv)):
            difference = max(shipmv[z], i.mv) - min(shipmv[z], i.mv)
            if difference < defaultship[1]:
                defaultship = (z, difference)

        if checkmove(i, shiplist[defaultship[0]]):
            assign(shiplist[defaultship[0]], i)
        else:
            extralist.append(i)

    finallist = []
    for c in extralist:
        shipmv = [x.mv for x in shiplist]
        while True:
            defaultship = (0, 400)

            for z in range(len(shipmv)):
                difference = max(shipmv[z], i.mv) - min(shipmv[z], i.mv)
                if difference < defaultship[1]:
                    defaultship = (z, difference)

            if checkmove(i, shiplist[defaultship[0]]):
                assign(shiplist[defaultship[0]], i)
                break
            else:
                shipmv.pop(defaultship[0])
            if len(shipmv) == 0:
                finallist.append(i)
                break

    # for y in shiplist:
        # print('ship' + str(y.name) + str(len(y.assigned)) +
        #      '    ' + str(y.payload) + ' ' + str(y.volume))
    # print('--------------------------------------------')
    #print('finallistlength:' + str(len(finallist)))
    # print(shiplist[0].mv)
    return solution(shiplist)


def dhlonsteroids(shiplist, parcellist):
    sol = (0, 0, {})
    currentsol = dhl(shiplist, parcellist)
    currentcost = calculatetotal(shiplist)
    print(currentcost)
