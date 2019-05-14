from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import checkmove, possiblemovesA
from code.helperfunctions.assign import assign
from code.helperfunctions.assign import solution, clearships, assignfromdict
import random
import pickle
import copy


def ups(shiplist, cargolist):
    return rnjesus(shiplist, cargolist)


def randomsolver(shiplist, parcellist):
    movelist = [1]
    while movelist != []:
        movelist = possiblemovesA(shiplist, parcellist)
        if movelist != []:
            randomchoice = random.randint(0, len(movelist))
            randomchoice -= 1
            move = movelist[randomchoice]
            assign(move[0], move[1])
            parcellist.remove(move[1])
    totalnumber = 0
    for i in shiplist:
        totalnumber += len(i.assigned)
    # clearships(shiplist)
    return totalnumber


def rnjesus(shiplist, cargolist):
    topsolutionnumber = 0
    topsolution = {}
    for i in range(0, 20000):
        deeplist = copy.deepcopy(cargolist)
        solutions = randomsolver(shiplist, deeplist)
        if solutions > topsolutionnumber:
            topsolutionnumber = solutions
            topsolution = shiplist
            pickle.dump(topsolution, open('topsolutionwithrnjesuss.p', 'wb'))
        clearships(shiplist)
    # pickle.dump(topsolution, open('topsolutionwithrnjesus.p', 'wb'))
    # open deze met
    # laad = pickle.load(open("topsolutionwithrnjesus.p", "rb"))
    return topsolutionnumber
