import numpy as np
import pandas as pd
import random
from code.helperfunctions.assign import assign, loadstate, clearships, solution, calculatetotal
from code.helperfunctions.possiblemoves import checkmove
from code.classes.spacecraft import Spacecraft

def planetexpress(shiplist, parcellist):
    selectedlist = []
    countrydict = {}
    countryships = {}
    c = 0
    for i in shiplist:
        countrydict[i.nation] = 0
        if i.nation in countryships.keys():
            worklist = countryships[i.nation]
            worklist.append(i)
            countryships[i.nation] = worklist
        else:
            countryships[i.nation] = [i]

    for i in parcellist:
        namelist = [x.name for x in selectedlist]
        ship = calcuateoptimal(i, shiplist)
        bool = False
        lowestpartner = min(countrydict, key=countrydict.get)
        difference = countrydict[ship.nation] - countrydict[lowestpartner]
        if ship.name in namelist:
            indexes = []
            for z in range(len(namelist)):
                if namelist[z] == ship.name:
                    indexes.append(z)

            for y in indexes:
                if checkmove(i, selectedlist[z]):
                    assign(selectedlist[z], i)
                    bool = True
                    break
            if bool == False:
                if difference > 0:
                    if len(countryships[lowestpartner]) > 1:
                        ship = calcuateoptimal(i,countryships[lowestpartner])
                    else:
                        ship = countryships[lowestpartner][0]

                spacecraft = Spacecraft(ship.name, ship.nation, ship.payload,
                                        ship.volume, ship.mass, ship.basecost, ship.ftw)
                newnumber = countrydict[ship.nation]
                newnumber += 1
                countrydict[ship.nation] = newnumber
                assign(spacecraft, i)
                selectedlist.append(spacecraft)
        else:
            if difference > 0:
                if len(countryships[lowestparner]) > 1:
                    ship = calculateoptimal(i,countryships[lowestparner])
                else:
                    ship = countryships[lowestparner][0]
                    print(ship)
            spacecraft = Spacecraft(ship.name, ship.nation, ship.payload,
                                    ship.volume, ship.mass, ship.basecost, ship.ftw)
            newnumber = countrydict[ship.nation]
            newnumber += 1
            countrydict[ship.nation] = newnumber
            assign(spacecraft, i)
            selectedlist.append(spacecraft)




    print(c)
    print(countrydict)
    print("amount of ships: " + str(len(selectedlist)))
    print("total costs: " + str(calculatetotal(selectedlist)))
    return solution(selectedlist)       #return the found solution in dictionary
                                        #form  to be able to work with later



def calcuateoptimal(parcel, shiplist):
    defaultship = (0, 400)
    shipmv = [x.mv for x in shiplist]
    for z in range(len(shipmv)):
        difference = max(shipmv[z], parcel.mv) - min(shipmv[z], parcel.mv)
        if difference < defaultship[1]:
            defaultship = (z, difference)

    return shiplist[defaultship[0]]
