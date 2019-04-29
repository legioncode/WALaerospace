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


def possibleswaps(shipdict):
    newlist = []
    newship = []
    for y in shipdict.keys():
        newlist.append(y)
    random.shuffle(newlist)
    newship = newlist[0].assigned
    removed_parcel = newship.pop()
    print(removed_parcel.ship.name)
    undomove(newlist[0], removed_parcel)
    for i in newlist:
        print(i.name)
    if checkmove(removed_parcel, newlist[1]):
        print('j')
        assign(newlist[1], removed_parcel)
        print('YAY!')
    elif checkmove(removed_parcel, newlist[2]):
        print('k')
        assign(newlist[2], removed_parcel)
        print('YAY!')
    elif checkmove(removed_parcel, newlist[3]):
        print('f')
        assign(newlist[3], removed_parcel)
        print('YAY!')
    else:
        print(removed_parcel.id, removed_parcel.mass, removed_parcel.size, removed_parcel.ship.name)
        print("There isn't any solution found")


def checkmove(parcel, ship):
    if parcel.mass <= ship.payload and parcel.size <= ship.volume:
        return True
    else:
        return False
