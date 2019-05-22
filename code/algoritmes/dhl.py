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
    """Takes as input a clear shiplist and parcellist. Greedily assigns parcels to spacecrafts, based on mass-volume ratio.
    Returns a shiplist of the solution."""
    # keep track of remainders
    extralist = []

    # for each parcel, find the best move based on mass-volume ratio
    for i in parcellist:
        shipmv = [x.mv for x in shiplist]
        defaultship = (0, 400)

        for z in range(len(shipmv)):
            difference = max(shipmv[z], i.mv) - min(shipmv[z], i.mv)
            if difference < defaultship[1]:
                defaultship = (z, difference)

        # check if the move is possible, else make this parcel a remainder
        if checkmove(i, shiplist[defaultship[0]]):
            assign(shiplist[defaultship[0]], i)
        else:
            extralist.append(i)

    # keep track of final remainders
    finallist = []

    # for each remainder, find a move, beginning with the best move possible based on mass-volume ratio
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
    """Takes as input a clear shiplist and parcellist. Generates n dhl solutions.
    Writes the shiplist of the best found solution to a pickle file the filename of which is returned ."""
    # get user input
    n = int(input("How many times do you want to run this algorithm: "))
    while n == "":
        n = int(input("How many times do you want to run this algorithm: "))
    filename = input("Please name how you want to save this solution: ")
    while filename == "":
        filename = input("Please name how you want to save this solution: ")
    picklename = str(f"results/Newsolutions/{filename}") + '.p'

    # keep track of the best solution
    sol = (0, 0, {})

    # run dhl n times, save the best found solution
    for i in range(n):
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
