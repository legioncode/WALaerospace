from code.helperfunctions.possiblemoves import checkmove, possiblemovesA
from code.helperfunctions.assign import assign
from code.helperfunctions.sort import sortParcels, sortSpacecrafts
import random
import pickle

def assignRemainders(shiplist, extralist):
    """Randomly assigns remainders if possible"""
    possiblelist = [1]
    while len(possiblelist) != 0:
        possiblelist = possiblemovesA(shiplist, extralist)
        if len(possiblelist) == 0:
            break
        chosenmove = possiblelist[0]
        assign(chosenmove[0], chosenmove[1])
        extralist.remove(chosenmove[1])

def postnl(shiplist, parcellist):
    """Greedy algorithm to assign parcels to spacecrafts"""
    # get sorted lists
    sorted_parcels = sortParcels(parcellist)
    sorted_ships = sortSpacecrafts(shiplist)

    # keep track of remainders
    remainders = []

    # get the left half of the shiplist, from middle to left-end
    halfcrafts = len(sorted_ships) / 2
    leftcrafts = sorted_ships[0: int(halfcrafts)]
    leftcrafts.reverse()

    # get the left half of the parcellist, from middle to left-end
    halfparcels = len(sorted_parcels) / 2
    worklistleft = sorted_parcels[0: int(halfparcels)]
    worklistleft.reverse()

    # append parcels from left half of parcellist to ships from left half of shiplist
    for i in range(int(halfparcels)):
        assigned = False
        for ship in leftcrafts:
            if checkmove(worklistleft[i], ship):
                assign(ship, worklistleft[i])
                assigned = True
                break
        if assigned == False:
            remainders.append(worklistleft[i])

    # get the right half of the parcellist, from middle to right-end
    worklistright = sorted_parcels[int(halfparcels):]

    # append parcels from half of both the parcel- and shiplist, back to the right end of both lists
    for i in range(int(halfparcels)):
        assigned = False
        for ship in sorted_ships[int(halfcrafts):]:
            if checkmove(worklistright[i], ship):
                assign(ship, worklistright[i])
                assigned = True
                break
        if assigned == False:
            remainders.append(worklistright[i])

    # try to assign remainders
    assignRemainders(shiplist, remainders)

    # save shiplist of solution as a pickle file
    filename = input("Please name how you want to save this solution: ")
    while filename == "":
        filename = input("Please name how you want to save this solution: ")
    picklename = str(filename) + '.p'
    pickle.dump(shiplist, open(picklename, 'wb'))
    return picklename
