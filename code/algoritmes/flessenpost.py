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
        #print(f"possiblelist = {possiblelist}")
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
    extra = []
    length = len(sorted_parcels)
    #worklist = sorted_parcels[0:int(length)]
    for parcel in reversed(range(len(sorted_parcels))):
        #print(f"parcel {parcel}")
        #print(f"mass = {sorted_parcels[parcel].mass}")
        if sorted_parcels[parcel].mw > 1600:
            print("te groot")
            remainders.append(sorted_parcels[parcel])
        elif checkmove(sorted_parcels[parcel], sorted_ships[3]):
            assign(sorted_ships[3], sorted_parcels[parcel])
        elif checkmove(sorted_parcels[parcel], sorted_ships[2]):
            assign(sorted_ships[2], sorted_parcels[parcel])
        elif checkmove(sorted_parcels[parcel], sorted_ships[1]):
            assign(sorted_ships[1], sorted_parcels[parcel])
        elif checkmove(sorted_parcels[parcel], sorted_ships[0]):
            assign(sorted_ships[0], sorted_parcels[parcel])
        else:
            remainders.append(sorted_parcels[parcel])

    print("---------------------------------------")
    print(f"remainders1: {len(remainders)}")
    #print(f"space0 assigned/weight/vol: {sorted_ships[0].name}{len(sorted_ships[0].assigned)}/{sorted_ships[0].payload}/{sorted_ships[0].volume}")
    #print(f"space1 assigned/weight/vol: {sorted_ships[1].name}{len(sorted_ships[1].assigned)}/{sorted_ships[1].payload}/{sorted_ships[1].volume}")
    #print(f"space2 assigned/weight/vol: {sorted_ships[2].name}{len(sorted_ships[2].assigned)}/{sorted_ships[2].payload}/{sorted_ships[2].volume}")
    #print(f"space3 assigned/weight/vol: {sorted_ships[3].name}{len(sorted_ships[3].assigned)}/{sorted_ships[3].payload}/{sorted_ships[3].volume}")
    #print(possiblemovesA(shiplist, remainders))
    dofirstmove(shiplist, remainders)
