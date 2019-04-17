from code.helperfunctions.possiblemoves import checkmove, possiblemovesA
from code.helperfunctions.assign import assign
import random

def sortparcels(parcellist):
    sorted_parcels = sorted(parcellist, key=lambda cargo: cargo.mw, reverse=False)
    return sorted_parcels

def sortspacecrafts(shiplist):
    sorted_ships = sorted(shiplist, key=lambda spacecraft: spacecraft.mw, reverse=False)
    return sorted_ships

def dorandommove(shiplist, extralist):
    possiblelist =[1]
    while possiblelist != []:
        possiblelist = possiblemovesA(shiplist, extralist)
        (print(f"possiblelist={possiblelist}"))
        chosenmove = possiblelist[random.randint(0,len(possiblelist))]
        print(f"chosenmove0cargo {chosenmove[0]}")
        print(f"chosenmove1space {chosenmove[1]}")
        assign(chosenmove[1],chosenmove[0])
        remainders.remove(chosenmove[0])
    print(f"remainders2: {len(remainders)}")

def postnl(shiplist, parcellist):
    # get sorted lists
    sorted_parcels = sortparcels(parcellist)
    sorted_ships = sortspacecrafts(shiplist)

    # create an extra list for remaining parcels
    remainders = []

    # start iterating back from half of list, append to spacecrafts 0 & 1
    half = len(sorted_parcels) / 2
    worklist = sorted_parcels[0: int(half)]
    for parcel in range(len(worklist)):
        parcel -= (parcel+1)
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
    dorandommove(shiplist, remainders)
