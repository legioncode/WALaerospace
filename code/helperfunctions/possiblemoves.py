from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.assign import assign
import random


def possiblemovesA(shiplist, parcellist):
    possiblemoves = []
    for i in parcellist:
        for x in shiplist:
            if i.mass <= x.payload and i.size <= x.volume:
                possiblemoves.append((x, i))
    return possiblemoves


<<<<<<< HEAD
=======
def possiblemovesB(shiplist, parcellist):
    possiblemoves = {}
    for i in parcellist:
        for x in shiplist:
            if i.mass <= x.payload and i.size <= x.volume:
                if i in possiblemoves.keys():
                    spacelist = possiblemoves[i]
                    spacelist.append(x)
                    possiblemoves[i] = spacelist
                else:
                    possiblemoves[i] = [x]
    return possiblemoves


def possiblemovesC(shiplist, parcellist):
    possiblemoves = {}
    for i in parcellist:
        for x in shiplist:
            if i.mass <= x.payload and i.size <= x.volume:
                if x in possiblemoves.keys():
                    cargolist = possiblemoves[x]
                    cargolist.append(i)
                    possiblemoves[x] = cargolist
                else:
                    possiblemoves[x] = [i]
    return possiblemoves


def possibleswaps(shipdict):
    for i in shipdict:
        if i.name == 'Cygnus':
            for a in i.assigned:
                removed_Cygnus = i.assigned.pop((random.randint(0, len(i.assigned)) - 1))
        elif i.name == 'Progress':
            for a in i.assigned:
                removed_Progress = i.assigned.pop((random.randint(0, len(i.assigned)) - 1))
        elif i.name == 'Kounotori':
            for a in i.assigned:
                removed_Kounotori = i.assigned.pop((random.randint(0, len(i.assigned)) - 1))
        elif i.name == 'Dragon':
            for a in i.assigned:
                removed_Dragon = i.assigned.pop((random.randint(0, len(i.assigned)) - 1))
        else:
            break
        if i.name == 'Cygnus':
            print(i.assigned)
        # if checkmove(removed_Cygnus, (i.name == 'Progress')) == True:
        #        assign(removed_Cygnus, (i.name == 'Progress'))
        # elif checkmove(removed_Cygnus)


>>>>>>> 84b3be91bf2a857bcaaedb1f83c044924fb075cf
def checkmove(parcel, ship):
    if parcel.mass <= ship.payload and parcel.size <= ship.volume:
        return True
    else:
        return False
