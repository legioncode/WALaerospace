from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft


def possiblemovesA(shiplist, parcellist):
    possiblemoves = []
    for i in parcellist:
        for x in shiplist:
            if i.mass <= x.payload and i.size <= x.volume:
                possiblemoves.append((x, i))
    return possiblemoves


def checkmove(parcel, ship):
    if parcel.mass <= ship.payload and parcel.size <= ship.volume:
        return True
    else:
        return False
