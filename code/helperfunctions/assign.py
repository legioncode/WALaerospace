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

def totalcost(shiplist) =
    
