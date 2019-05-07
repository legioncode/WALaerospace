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
    # ship.ratio()


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


def updatemv(shiplist):
    return [x.mv for x in shiplist]


def clearships(shiplist):
    for i in shiplist:
        i.assigned = []
        i.payload = i.firstpayload
        i.volume = i.firstvolume
        i.mv = i.payload / float(i.volume)


def assignfromdict(shipdict):
    for i in shipdict.keys():
        shipdict[i].assigned = shipdict[i]


def calculatetotal(shiplist):
    cost = 0
    for i in shiplist:
        cost += i.cost
    return cost


def loadstate(solution, shiplist):
    for i in solution.keys():
        for x in shiplist:
            if i.name == x.name:
                x.assigned = solution[i]
                x.ratio()


def calculatepackages(shiplist):
    return sum(len(i.assigned) for i in shiplist)
