from code.helperfunctions.possiblemoves import checkmove, possiblemovesA
from code.helperfunctions.assign import assign, calculatetotal
import random
from code.classes.spacecraft import Spacecraft


def sortparcels(parcellist):
    sorted_parcels = sorted(parcellist, key=lambda cargo: cargo.mv, reverse=False)
    return sorted_parcels


def sortspacecrafts(shiplist):
    sorted_ships = sorted(shiplist, key=lambda spacecraft: spacecraft.mv, reverse=False)
    return sorted_ships


def MoveRemainders(shiplist, extralist):
    possiblelist = [1]
    while len(possiblelist) != 0:
        possiblelist = possiblemovesA(shiplist, extralist)
        if len(possiblelist) == 0:
            break
        chosenmove = possiblelist[0]
        assign(chosenmove[0], chosenmove[1])
        extralist.remove(chosenmove[1])
    print(f"remainders after reassignment: {len(extralist)}")
    for i in extralist:
        print(f"overgebleven = {i.id}")


def postnl(shiplist, parcellist):
    # get sorted lists
    sorted_parcels = sortparcels(parcellist)
    sorted_ships = sortspacecrafts(shiplist)


    # create an extra list for remaining parcels
    remainders = []

    # start iterating back from half of list, append to spacecrafts 0 & 1
    halfcrafts = len(sorted_ships) / 2
    leftcrafts = sorted_ships[0: int(halfcrafts)]
    leftcrafts.reverse()
    half = len(sorted_parcels) / 2
    worklist = sorted_parcels[0: int(half)]
    worklist.reverse()

    for i in range(int(half)):
        assigned = False
        for ship in leftcrafts:
            if checkmove(worklist[i], ship):
                assign(ship, worklist[i])
                assigned = True
                break
        if assigned == False:
            remainders.append(worklist[i])

    print(f"tussenstand {len(remainders)}")

    # start iterating at half of list, append to spacecrafts 2 & 3
    worklist2 = sorted_parcels[int(half):]
    for i in range(int(half)):
        assigned = False
        for ship in sorted_ships[int(halfcrafts):]:
            if checkmove(worklist2[i], ship):
                assign(ship, worklist2[i])
                assigned = True
                break
        if assigned == False:
            remainders.append(worklist2[i])

    # prints
    print(f"remainders before reassignment: {len(remainders)}")
    MoveRemainders(shiplist, remainders)
    print(f"{sorted_ships[0].name} costs {sorted_ships[0].cost} and carries {len(sorted_ships[0].assigned)}")
    print(f"{sorted_ships[1].name} costs {sorted_ships[1].cost} and carries {len(sorted_ships[1].assigned)}")
    print(f"{sorted_ships[2].name} costs {sorted_ships[2].cost} and carries {len(sorted_ships[2].assigned)}")
    print(f"{sorted_ships[3].name} costs {sorted_ships[3].cost} and carries {len(sorted_ships[3].assigned)}")
    return shiplist
