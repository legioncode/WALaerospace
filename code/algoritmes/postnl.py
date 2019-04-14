from code.helperfunctions.readers import *

def postnl(shiplist, parcellist):
    # sort the parcellist based on mw ratio
    sorted_parcels = sorted(parcellist, key=lambda cargo: cargo.mw, reverse=False)
    sorted_ships = sorted(shiplist, key=lambda spacecraft: spacecraft.mw, reverse=False)

    # create an extra list for remaining parcels
    remainders = []

    # start iterating at half of list, append to spacecrafts 3 & 4
    half = len(sorted_parcels) / 2
    for parcel in sorted_parcels[half:]:
        if checkmove(parcel, sorted_ships[2]):
            assign(shiplist[], parcel)
        elif checkmove(parcel, sorted_ships[3]):
            assign(shiplist[], parcel)
        else:
            remainders.append(parcel)

    # start iterating back from half of list, append to spacecrafts 1 & 2
    half = len(sorted_parcels) / 2
    for parcel in sorted_parcels[half, 0, -1]:
        if checkmove(parcel, sorted_ships[1]):
            assign(shiplist[], parcel)
        elif checkmove(parcel, sorted_ships[0]):
            assign(shiplist[], parcel)
        else:
            remainders.append(parcel)
