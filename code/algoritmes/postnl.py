from code.helperfunctions.readers import *
from code.helperfunctions.possiblemoves import checkmove
from code.helperfunctions.assign import assign

def postnl(shiplist, parcellist):
    # sort the parcellist based on mv ratio
    sorted_parcels = sorted(parcellist, key=lambda cargo: cargo.mw, reverse=False)
    sorted_ships = sorted(shiplist, key=lambda spacecraft: spacecraft.mw, reverse=False)
    # create an extra list for remaining parcels
    remainders = []

    # start iterating at half of list, append to spacecrafts 3 & 4
    half = len(sorted_parcels) / 2
    for parcel in sorted_parcels[int(half):]:
        if checkmove(parcel, sorted_ships[2]):
            assign(sorted_ships[2], parcel)
        elif checkmove(parcel, sorted_ships[3]):
            assign(sorted_ships[3], parcel)
        else:
            remainders.append(parcel)

    # start iterating back from half of list, append to spacecrafts 1 & 2
    worklist = sorted_parcels[0: int(half)]
    for parcel in range(len(worklist)):
        parcel -= (parcel+1)
        if checkmove(worklist[parcel], sorted_ships[1]):
            assign(sorted_ships[1], worklist[parcel])
        elif checkmove(worklist[parcel], sorted_ships[0]):
            assign(sorted_ships[0], worklist[parcel])
        else:
            remainders.append(worklist[parcel])

    # prints
    print(f"remainders: {len(remainders)}")
    print(f"space2: {sorted_ships[2].assigned}")
    print(f"space3: {sorted_ships[3].assigned}")
    print(f"space1: {sorted_ships[1].assigned}")
    print(f"space0: {sorted_ships[0].assigned}")
