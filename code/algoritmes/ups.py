from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
import numpy as np
import pandas as pd
from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.helperfunctions.possiblemoves import checkmove, possiblemovesA
from code.helperfunctions.assign import assign
from code.helperfunctions.assign import returnLastParcel, solution, clearships
import random


# def ups(shiplist, parcellist):

def randomsolver(shiplist, parcellist):
    movelist = [1]
    while movelist != []:
        movelist = possiblemovesA(shiplist, parcellist)
        if movelist != []:
            randomchoice = random.randint(0, len(movelist))
            randomchoice -= 1
            move = movelist[randomchoice]
            assign(move[0], move[1])
    totalnumber = 0
    for i in shiplist:
        totalnumber += len(i.assigned)
    return totalnumber


def rnjesus(shiplist, parcellist):
    topsolutionnumber = 0
    topsolution = {}
    for i in range(0, 500):
        solutions = randomsolver(shiplist, parcellist)
        if solutions > topsolutionnumber:
            topsolutionnumber = solutions
            topsolution = solution(shiplist)
        clearships(shiplist)
    return topsolutionnumber
