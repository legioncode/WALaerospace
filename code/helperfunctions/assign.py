from code.classes.cargo import *
from code.classes.spacecraft import *


def assign(ship, parcel):
    worklist = ship.assigned
    worklist.append(parcel)
    ship.assigned = worklist
    ship.volume = ship.volume - parcel.size
    ship.payload = ship.payload - parcel.mass
    ship.mass = ship.mass + parcel.mass
    ship.ratio()


def returnLastParcel(ship):
    parcel = ship.assigned.pop(-1)
    ship.volume = ship.volume + parcel.size
    ship.payload = ship.payload + parcel.mass
    ship.mass = ship.mass - parcel.mass
    ship.ratio()
    return parcel


def solution(shiplist):
    solutiondict = {}
    for i in shiplist:
        solutiondict[i] = i.assigned
    return solutiondict


def updatemw(shiplist):
    return [x.mw for x in shiplist]


def clearships(shiplist):
    for i in shiplist:
        i.clear()


def assignfromdict(shipdict):
    for i in shipdict.keys():
        shipdict[i].assigned = shipdict[i]

def calculatetotal(shiplist):
    return sum([i.calculate for i in shiplist])
# def totalcost(shiplist) =
