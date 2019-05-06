from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.assign import assign, undomove
import random


def possiblemovesA(shiplist, parcellist):
    possiblemoves = []
    for i in parcellist:
        for x in shiplist:
            if i.mass <= x.payload and i.size <= x.volume:
                possiblemoves.append((x, i))
    return possiblemoves


def depthmoves(shiplist, parcellist, depth):
    possiblemoves = []
    for i in parcellist:
        for x in shiplist:
            if i.mass <= x.payload and i.size <= x.volume:
                possiblemoves.append((x, i, depth))
    return possiblemoves


def possiblemovesB(shiplist, parcellist):
    possiblemoves = {}
    for i in parcellist:
        for x in shiplist:
            if i.mass <= x.payload and i.size <= x.volume:
                if i in possiblemoves.keys():
                    spacelist = possiblemoves[i]
                    spacelist.append(x)
                    possiblemoves[i] = spacelist
                else:
                    possiblemoves[i] = [x]
    return possiblemoves


def possiblemovesC(shiplist, parcellist):
    possiblemoves = {}
    for i in parcellist:
        for x in shiplist:
            if i.mass <= x.payload and i.size <= x.volume:
                if x in possiblemoves.keys():
                    cargolist = possiblemoves[x]
                    cargolist.append(i)
                    possiblemoves[x] = cargolist
                else:
                    possiblemoves[x] = [i]
    return possiblemoves


def possiblemovecost(shiplist, parcellist):
    possiblemoves = []
    for i in parcellist:
        for x in shiplist:
            if i.mass <= x.payload and i.size <= x.volume:
                z = calculatemovecost(x, i)
                possiblemoves.append((x, i, z))
    return possiblemoves

 # je doet nu alleen swaps die mogelijk zijn, wat niet perse een ideale oplossing oplever


def possibleswaps(shipdict):
    newlist = []
    for y in shipdict.keys():
        newlist.append(y)
    random.shuffle(newlist)
    '''for i in range(0, 3):
        for a in newlist[i].assigned:

        if checkmove(parcel1, newlist[1]):
            print('j')
            assign(newlist[1], parcel1)
            print('YAY!')
        elif checkmove(parcel1, newlist[2]):
            print('k')
            assign(newlist[2], parcel1)
            print('YAY!')
        elif checkmove(parcel1, newlist[3]):
            print('f')
            assign(newlist[3], parcel1)
            print('YAY!')
        else:
            print(parcel1.id, parcel1.mass, parcel1.size)
            print("There isn't any solution found")'''


def checkmove(parcel, ship):
    if parcel.mass <= ship.payload and parcel.size <= ship.volume:
        return True
    else:
        return False


def calculatemovecost(ship, parcel):
    return (parcel.mass * ship.ftw / (1 - ship.ftw) * 1000)
