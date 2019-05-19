from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import checkmove, possiblemovesA
from code.helperfunctions.assign import assign
from code.helperfunctions.assign import solution, clearships, assignfromdict
import random
import pickle
import copy


def ups(shiplist, cargolist):
    max = int(input("How many times do you want to run this algorithm: "))
    while max == "":
        max = int(input("How many times do you want to run this algorithm: "))
    filename = input("Please name how you want to save this solution: ")
    while filename == "":
        filename = input("Please name how you want to save this solution: ")
    picklename = str(filename) + '.p'
    topsolutionnumber = 0
    topsolution = {}
    for i in range(0, max):
        deeplist = copy.deepcopy(cargolist)
        solutions = randomsolver(shiplist, deeplist)
        if solutions > topsolutionnumber:
            topsolutionnumber = solutions
            topsolution = shiplist
            pickle.dump(topsolution, open(picklename, 'wb'))
        clearships(shiplist)
    return picklename

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
