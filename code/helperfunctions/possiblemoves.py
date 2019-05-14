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


def checkmove(parcel, ship):
    if parcel.mass <= ship.payload and parcel.size <= ship.volume:
        return True
    else:
        return False


def calculatemovecost(ship, parcel):
    return (parcel.mass * ship.ftw / (1 - ship.ftw) * 1000)
