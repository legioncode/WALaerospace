from code.helperfunctions.assign import assign
from code.helperfunctions.assign import solution
from code.helperfunctions.assign import calculateoptimal
from code.helperfunctions.assign import calculatetotal
from code.helperfunctions.possiblemoves import checkmove
from code.classes.spacecraft import Spacecraft
import random

def ns(shiplist, parcellist):
    '''ns takes in two arguments, a list of ship objects and a list of
       cargo objects. it assigns parcels to spaceships untill they're full.
       after a spaceship has been filled it chooses a random new ship'''
    randomchoice = random.randint(0, len(shiplist) - 1)
    ship = shiplist[randomchoice]
    spacecraft = Spacecraft(ship.name, ship.nation, ship.payload,
    ship.volume, ship.mass, ship.basecost,
    ship.ftw)
    fleet = [spacecraft]

    c = 0
    for i in parcellist:
        if checkmove(i, fleet[-1]):
            assign(fleet[-1], i)
            c += 1
        else:
            randomchoice = random.randint(0, len(shiplist) - 1)
            ship = shiplist[randomchoice]
            spacecraft = Spacecraft(ship.name, ship.nation, ship.payload,
            ship.volume, ship.mass, ship.basecost,
            ship.ftw)
            fleet.append(spacecraft)
            assign(fleet[-1], i)
            c += 1

    print(calculatetotal(fleet))
