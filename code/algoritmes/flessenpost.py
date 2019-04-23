from code.helperfunctions.possiblemoves import checkmove, possiblemovesA
from code.helperfunctions.assign import assign
import random


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

def flessenpost(shiplist, parcellist):
    # get sorted lists
    sorted_parcels = sortparcels(parcellist)
    sorted_ships = sortspacecrafts(shiplist)

    # create an extra list for remaining parcels
    remainders = []
    length = len(sorted_parcels)
    print(f"length = {length}")
    worklist = sorted_parcels[0:int(length)]
    for parcel in range(len(worklist)):
        parcel -= (parcel+1)
        if checkmove(worklist[parcel], sorted_ships[3]):
            assign(sorted_ships[3], worklist[parcel])
        elif checkmove(worklist[parcel], sorted_ships[2]):
            assign(sorted_ships[2], worklist[parcel])
        elif checkmove(worklist[parcel], sorted_ships[1]):
            assign(sorted_ships[1], worklist[parcel])
        elif checkmove(worklist[parcel], sorted_ships[0]):
            assign(sorted_ships[0], worklist[parcel])
        else:
            print("hoi")
            remainders.append(worklist[parcel])

    print(f"remainders1: {len(remainders)}")
    print(f"space0 assigned/weight/vol: {sorted_ships[0].name}{len(sorted_ships[0].assigned)}/{sorted_ships[0].payload}/{sorted_ships[0].volume}")
    print(f"space1 assigned/weight/vol: {sorted_ships[1].name}{len(sorted_ships[1].assigned)}/{sorted_ships[1].payload}/{sorted_ships[1].volume}")
    print(f"space2 assigned/weight/vol: {sorted_ships[2].name}{len(sorted_ships[2].assigned)}/{sorted_ships[2].payload}/{sorted_ships[2].volume}")
    print(f"space3 assigned/weight/vol: {sorted_ships[3].name}{len(sorted_ships[3].assigned)}/{sorted_ships[3].payload}/{sorted_ships[3].volume}")
    #print(possiblemovesA(shiplist, remainders))
    #dofirstmove(shiplist, remainders)
