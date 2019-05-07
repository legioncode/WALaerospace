from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import checkmove, possiblemovesA, possibleswaps
from code.helperfunctions.assign import assign
from code.helperfunctions.assign import solution, clearships, assignfromdict
import random


def ups(shiplist, parcellist):
    return rnjesus(shiplist, parcellist)


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
    for i in range(0, 20000):
        solutions = randomsolver(shiplist, parcellist)
        if solutions > topsolutionnumber:
            topsolutionnumber = solutions
            topsolution = solution(shiplist)
        clearships(shiplist)
    return topsolutionnumber
