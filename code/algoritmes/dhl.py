import random
from code.helperfunctions.assign import assign, solution, returnLastParcel, calculatetotal, clearships
from code.helperfunctions.possiblemoves import checkmove
from code.helperfunctions.readers import loadships
from code.helperfunctions.readers import loadparcels
import pandas as pd
import numpy as np
from code.classes.spacecraft import *
from code.classes.cargo import *
import pickle


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
    return shiplist


def dhlonsteroids(shiplist, parcellist):
    max = int(input("How many times do you want to run this algorithm: "))
    while max == "":
        max = int(input("How many times do you want to run this algorithm: "))
    filename = input("Please name how you want to save this solution: ")
    while filename == "":
        filename = input("Please name how you want to save this solution: ")
    picklename = str(filename) + '.p'
    sol = (0, 0, {})
    for i in range(max):
        random.shuffle(parcellist)
        currentsol = dhl(shiplist, parcellist)
        currentcost = calculatetotal(shiplist)
        xlist = []
        for z in currentsol:
            for y in z.assigned:
                xlist.append(y)
        if len(xlist) == sol[1]:
            if currentcost < sol[1]:
                sol = (len(xlist), currentcost, currentsol)
                pickle.dump(sol[2], open(picklename, 'wb'))
        elif len(xlist) > sol[1]:
            sol = (len(xlist), currentcost, currentsol)
            pickle.dump(sol[2], open(picklename, 'wb'))
        clearships(shiplist)

    return picklename
