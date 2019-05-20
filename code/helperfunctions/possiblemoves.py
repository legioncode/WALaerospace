from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.assign import assign, undomove
import random


def possiblemovesA(shiplist, parcellist):
    """Takes in a shiplist and a parcellist, generates and returns the possible moves."""
    possiblemoves = []
    for i in parcellist:
        for x in shiplist:
            if i.mass <= x.payload and i.size <= x.volume:
                possiblemoves.append((x, i))
    return possiblemoves


def possiblemovecost(shiplist, parcellist):
    """Takes in a shiplist and a parcellist, generates and returns the possible moves and their costs."""
    possiblemoves = []
    for i in parcellist:
        for x in shiplist:
            if i.mass <= x.payload and i.size <= x.volume:
                z = calculatemovecost(x, i)
                possiblemoves.append((x, i, z))
    return possiblemoves


def checkmove(parcel, ship):
    """Takes in a ship and a parcel, checks if this is a valid move and returns a boolean."""
    if parcel.mass <= ship.payload and parcel.size <= ship.volume:
        return True
    else:
        return False


def calculatemovecost(ship, parcel):
    """Takes in a ship and a parcel, generates and returns the cost of this move."""
    return (parcel.mass * ship.ftw / (1 - ship.ftw) * 1000)
