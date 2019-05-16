from code.helperfunctions.possiblemoves import checkmove, possiblemovesA
from code.helperfunctions.assign import assign
import random
import numpy as np


def sortparcels(parcellist):
    sorted_parcels = sorted(parcellist, key=lambda cargo: cargo.mv, reverse=False)
    return sorted_parcels


def sortspacecrafts(shiplist):
    sorted_ships = sorted(shiplist, key=lambda spacecraft: spacecraft.mv, reverse=False)
    return sorted_ships


def packRemainders(shiplist, extralist):
    possiblelist = [1]
    while len(possiblelist) != 0:
        possiblelist = possiblemovesA(shiplist, extralist)
        if len(possiblelist) == 0:
            break
        chosenmove = possiblelist[0]
        assign(chosenmove[0], chosenmove[1])
        extralist.remove(chosenmove[1])


def computeOutliers(parcellist):
    ratios = [parcel.mv for parcel in parcellist]
    q1 = np.percentile(ratios, 25)
    median = np.percentile(ratios, 50)
    q3 = np.percentile(ratios, 75)
    outlierbound = 1.5 * (q3 - q1) + q3
    return outlierbound


def flessenpost(shiplist, parcellist):
    # get sorted lists
    outlierbound = computeOutliers(parcellist)
    sorted_parcels = sortparcels(parcellist)
    sorted_parcels.reverse()
    sorted_ships = sortspacecrafts(shiplist)
    sorted_ships.reverse()
    # create an extra list for remaining parcels
    remainders = []
    outliers = []
    for parcel in range(len(sorted_parcels)):
        assigned = False
        if sorted_parcels[parcel].mv > outlierbound:
            outliers.append(sorted_parcels[parcel])
        for ship in sorted_ships:
            if checkmove(sorted_parcels[parcel], ship):
                assign(ship, sorted_parcels[parcel])
                assigned = True
                break
        if assigned == False:
            remainders.append(sorted_parcels[parcel])

    packRemainders(shiplist, remainders)
    packRemainders(shiplist, outliers)
    return shiplist
