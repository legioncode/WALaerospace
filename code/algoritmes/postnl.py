from code.helperfunctions.possiblemoves import checkmove, possiblemovesA
from code.helperfunctions.assign import assign, calculatetotal
import random
from code.classes.spacecraft import Spacecraft


def sortparcels(parcellist):
    sorted_parcels = sorted(parcellist, key=lambda cargo: cargo.mw, reverse=False)
    return sorted_parcels

def sortspacecrafts(shiplist):
    sorted_ships = sorted(shiplist, key=lambda spacecraft: spacecraft.mw, reverse=False)
    return sorted_ships

def dofirstmove(shiplist, extralist):
    possiblelist =[1]
    while len(possiblelist) != 0:
        possiblelist = possiblemovesA(shiplist, extralist)
        if len(possiblelist) == 0:
            break
        chosenmove = possiblelist[0]
        assign(chosenmove[0], chosenmove[1])
        extralist.remove(chosenmove[1])
    print(f"remainders3: {len(extralist)}")
    for i in extralist:
        print(f"overgebleven = {i.id}")

def postnl(shiplist, parcellist):
    # get sorted lists
    sorted_parcels = sortparcels(parcellist)
    sorted_ships = sortspacecrafts(shiplist)

    # create an extra list for remaining parcels
    remainders = []

    # start iterating back from half of list, append to spacecrafts 0 & 1
    half = len(sorted_parcels) / 2
    worklist = sorted_parcels[0: int(half)]
    for parcel in reversed(range(len(worklist))):
        if checkmove(worklist[parcel], sorted_ships[1]):
            assign(sorted_ships[1], worklist[parcel])
        elif checkmove(worklist[parcel], sorted_ships[0]):
            assign(sorted_ships[0], worklist[parcel])
        else:
            remainders.append(worklist[parcel])

    # start iterating at half of list, append to spacecrafts 2 & 3
    for parcel in sorted_parcels[int(half):]:
        if checkmove(parcel, sorted_ships[2]):
            assign(sorted_ships[2], parcel)
        elif checkmove(parcel, sorted_ships[3]):
            assign(sorted_ships[3], parcel)
        else:
            remainders.append(parcel)

    # prints
    print(f"remainders1: {len(remainders)}")
    #print(f"space2 assigned/weight/vol: {len(sorted_ships[2].assigned)}/{sorted_ships[2].payload}/{sorted_ships[2].volume}")
    #print(f"space3 assigned/weight/vol: {len(sorted_ships[3].assigned)}/{sorted_ships[3].payload}/{sorted_ships[3].volume}")
    #print(f"space0 assigned/weight/vol: {len(sorted_ships[0].assigned)}/{sorted_ships[0].payload}/{sorted_ships[0].volume}")
    #print(f"space1 assigned/weight/vol: {len(sorted_ships[1].assigned)}/{sorted_ships[1].payload}/{sorted_ships[1].volume}")
    #print(possiblemovesA(shiplist, remainders))
    dofirstmove(shiplist, remainders)
    print(f"{sorted_ships[0].name} costs {sorted_ships[0].cost}")
    print(f"{sorted_ships[1].name} costs {sorted_ships[1].cost}")
    print(f"{sorted_ships[2].name} costs {sorted_ships[2].cost}")
    print(f"{sorted_ships[3].name} costs {sorted_ships[3].cost}")
