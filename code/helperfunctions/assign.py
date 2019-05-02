from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
import copy

def assign(ship, parcel):
    worklist = ship.assigned
    worklist.append(parcel)
    ship.assigned = worklist
    ship.volume = ship.volume - parcel.size
    ship.payload = ship.payload - parcel.mass
    parcel.ship = ship
    ship.ratio()


def undomove(ship, parcel):
    if parcel in ship.assigned:
        newassign = ship.assigned.remove(parcel)
        ship.volume = ship.volume + parcel.size
        ship.payload = ship.payload + parcel.mass
        parcel.ship = None


def returnLastParcel(ship):
    parcel = ship.assigned.pop(-1)
    ship.volume = ship.volume + parcel.size
    ship.payload = ship.payload + parcel.mass
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
    cost = 0
    for i in shiplist:
        cost += i.cost
    return cost


def calculatepackages(shiplist):
    return sum(len(i.assigned) for i in shiplist)
