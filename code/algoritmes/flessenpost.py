from code.helperfunctions.possiblemoves import checkmove, possiblemovesA
from code.helperfunctions.assign import assign
import random

def sortparcels(parcellist):
    sorted_parcels = sorted(parcellist, key=lambda cargo: cargo.mv, reverse=False)
    return sorted_parcels


def sortspacecrafts(shiplist):
    sorted_ships = sorted(shiplist, key=lambda spacecraft: spacecraft.mv, reverse=False)
    return sorted_ships


def packremainders(shiplist, extralist):
    possiblelist = [1]
    while len(possiblelist) != 0:
        possiblelist = possiblemovesA(shiplist, extralist)
        #print(f"possiblelist = {possiblelist}")
        if len(possiblelist) == 0:
            break
        chosenmove = possiblelist[0]
        assign(chosenmove[0], chosenmove[1])
        extralist.remove(chosenmove[1])
    #print(f"remainders: {len(extralist)}")

def flessenpost(shiplist, parcellist):
    # get sorted lists
    sorted_parcels = sortparcels(parcellist)
    sorted_ships = sortspacecrafts(shiplist)
    # create an extra list for remaining parcels
    remainders = []
    outliers = []
    extra = []
    length = len(sorted_parcels)
    #worklist = sorted_parcels[0:int(length)]
    for parcel in reversed(range(len(sorted_parcels))):
        #print(f"parcel {parcel}")
        #print(f"mass = {sorted_parcels[parcel].mass}")
        if sorted_parcels[parcel].mv > 1600:
            outliers.append(sorted_parcels[parcel])
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
    #print(f"initial remainders: {len(remainders)}")

    packremainders(shiplist, remainders)
    packremainders(shiplist, outliers)
    return shiplist
