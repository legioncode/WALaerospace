from code.helperfunctions.possiblemoves import checkmove, possiblemovesA
from code.helperfunctions.assign import assign

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
    print(f"ultimateremainderschina: {len(extralist)}")

def chinapost(shiplist, parcellist):
    # get sorted lists
    sorted_parcels = sortparcels(parcellist)
    sorted_ships = sortspacecrafts(shiplist)

    # create an extra list for remaining parcels
    remainderschina = []

    # start iterating back from half of list, append to spacecrafts 0 & 1
    half = len(sorted_parcels) / 2
    worklist = sorted_parcels[0: int(half)]
    for parcel in range(len(worklist)):
        parcel -= (parcel+1)
        if checkmove(worklist[parcel], sorted_ships[1]):
            assign(sorted_ships[1], worklist[parcel])
            sorted_ships = sortspacecrafts(shiplist)
        elif checkmove(worklist[parcel], sorted_ships[0]):
            assign(sorted_ships[0], worklist[parcel])
            sorted_ships = sortspacecrafts(shiplist)
        else:
            remainderschina.append(worklist[parcel])

    # start iterating at half of list, append to spacecrafts 2 & 3
    for parcel in sorted_parcels[int(half):]:
        if checkmove(parcel, sorted_ships[2]):
            assign(sorted_ships[2], parcel)
            sorted_ships = sortspacecrafts(shiplist)
        elif checkmove(parcel, sorted_ships[3]):
            assign(sorted_ships[3], parcel)
            sorted_ships = sortspacecrafts(shiplist)
        else:
            remainderschina.append(parcel)

    # prints
    print(f"chinaremainders: {len(remainderschina)}")
    #print(f"space2: {len(sorted_ships[2].assigned)}")
    #print(f"space3: {len(sorted_ships[3].assigned)}")
    #print(f"space1: {len(sorted_ships[1].assigned)}")
    #print(f"space0: {len(sorted_ships[0].assigned)}")

    dofirstmove(shiplist, remainderschina)
