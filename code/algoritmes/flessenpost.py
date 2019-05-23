from code.helperfunctions.assign import assign
from code.helperfunctions.possiblemoves import checkmove
from code.helperfunctions.possiblemoves import possiblemovesA
from code.helperfunctions.sort import sortParcels
from code.helperfunctions.sort import sortSpacecrafts
import numpy as np
import pickle
import random


def assignRemainders(shiplist, extralist):
    """Takes as input a shiplist of a solution and a list of remaining parcels.
    Randomly assigns remainders if possible. Edits the shiplist."""
    possiblelist = [1]
    while len(possiblelist) != 0:
        possiblelist = possiblemovesA(shiplist, extralist)
        if len(possiblelist) == 0:
            break
        chosenmove = possiblelist[0]
        assign(chosenmove[0], chosenmove[1])
        extralist.remove(chosenmove[1])


def computeOutliers(parcellist):
    """Takes as input a parcellist. Computes outliers with high mass-volume
    ratios of the parcellist and returns the bound."""
    ratios = [parcel.mv for parcel in parcellist]
    q1 = np.percentile(ratios, 25)
    median = np.percentile(ratios, 50)
    q3 = np.percentile(ratios, 75)
    outlierbound = 1.5 * (q3 - q1) + q3
    return outlierbound


def flessenpost(shiplist, parcellist):
    """Takes as input a clear shiplist and parcellist. Greedily assigns parcels
    to spacecrafts, taking into consideration outliers. Saves the solution to a
    pickle file the filename of which is returned."""
    # get sorted outlierbound and reversed parcel- and shiplist
    outlierbound = computeOutliers(parcellist)
    sorted_parcels = sortParcels(parcellist)
    sorted_parcels.reverse()
    sorted_ships = sortSpacecrafts(shiplist)
    sorted_ships.reverse()

    # keep track of remaining parcels and outliers
    remainders = []
    outliers = []

    # assign parcels to ships beginning with the highest ratios, skip outliers
    for parcel in range(len(sorted_parcels)):
        assigned = False
        if sorted_parcels[parcel].mv > outlierbound:
            outliers.append(sorted_parcels[parcel])
        for ship in sorted_ships:
            if checkmove(sorted_parcels[parcel], ship):
                assign(ship, sorted_parcels[parcel])
                assigned = True
                break
        if assigned is False:
            remainders.append(sorted_parcels[parcel])

    # try to assign remainders
    assignRemainders(shiplist, remainders)

    # try to assign outliers
    assignRemainders(shiplist, outliers)

    # save shiplist of solution as a pickle file
    filename = input("Please name how you want to save this solution: ")
    while filename == "":
        filename = input("Please name how you want to save this solution: ")
    picklename = str(f"results/Newsolutions/{filename}.p")
    pickle.dump(shiplist, open(picklename, 'wb'))
    return picklename
