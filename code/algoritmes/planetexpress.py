from code.classes.spacecraft import Spacecraft
from code.helperfunctions.assign import assign
from code.helperfunctions.assign import calculateoptimal
from code.helperfunctions.assign import calculatetotal
from code.helperfunctions.assign import clearships
from code.helperfunctions.assign import loadstate
from code.helperfunctions.assign import solution
from code.helperfunctions.possiblemoves import checkmove
import numpy as np
import pandas as pd
import pickle
import random


def planetexpress(shiplist, parcellist):
    ''' Planetexpress is  a greedy algorithm for problem E of the spacefreight
        case. Planetexpres takes in two arguments, a list of shipobjects and
        a list of cargo objects.

        planetexpress creates a list of spaceships to assign the parcellist to
        based on the mass to volume ratio of spaceships and parcels.

        Planetexpress does this while also obiding to the constraint that every
        country with a ship doesnt launch more than 1 ship extra than any other
        country involed.

        Planetexpress returns a dictionary with the spaceship objects as keys
        and their assigned parcels as values. it also prints the amount of
        ships used and the total costs of launching the fleet.'''
    selectedlist = []     # the list that contains the fleet of spaceships
    countrydict = {}      # dictionary containing the N of launches per country
    countryships = {}     # the dictionary with countries and their ships
    c = 0
    for i in shiplist:         # starts up the countrydict
        countrydict[i.nation] = 0
        if i.nation in countryships.keys():
            worklist = countryships[i.nation]
            worklist.append(i)
            countryships[i.nation] = worklist
        else:
            countryships[i.nation] = [i]

    for i in parcellist:
        # turns the list of the current fleet into a list of classes
        namelist = [x.name for x in selectedlist]
        ship = calculateoptimal(i, shiplist)
        bool = False
        lowestpartner = min(countrydict, key=countrydict.get)
        difference = countrydict[ship.nation] - countrydict[lowestpartner]
        # checks if the matched ship is in fleetlist
        if ship.name in namelist:
            indexes = []
            for z in range(len(namelist)):
                if namelist[z] == ship.name:
                    indexes.append(z)
            # checks all ships of that class in the fleet list
            for y in indexes:
                if checkmove(i, selectedlist[z]):
                    assign(selectedlist[z], i)
                    bool = True
                    break
            if bool is False:
                if difference > 0:  # checks constraint
                    if len(countryships[lowestpartner]) > 1:
                        ship = calculateoptimal(i, countryships[lowestpartner])
                    else:
                        ship = countryships[lowestpartner][0]

                spacecraft = Spacecraft(ship.name, ship.nation, ship.payload,
                                        ship.volume, ship.mass, ship.basecost,
                                        ship.ftw)
                newnumber = countrydict[ship.nation]
                newnumber += 1
                countrydict[ship.nation] = newnumber
                assign(spacecraft, i)
                selectedlist.append(spacecraft)
        else:
            if difference > 0:
                if len(countryships[lowestparner]) > 1:
                    ship = calculateoptimal(i, countryships[lowestparner])
                else:
                    ship = countryships[lowestparner][0]
                    print(ship)
            spacecraft = Spacecraft(ship.name, ship.nation, ship.payload,
                                    ship.volume, ship.mass, ship.basecost,
                                    ship.ftw)
            newnumber = countrydict[ship.nation]
            newnumber += 1
            countrydict[ship.nation] = newnumber
            assign(spacecraft, i)
            selectedlist.append(spacecraft)

    sol = solution(selectedlist)
    filename = input("Please name how you want to save this solution: ")
    while filename == "":
        filename = input("Please name how you want to save this solution: ")
    picklename = str(f"results/Newsolutions/{filename}.p")
    pickle.dump(sol, open(picklename, 'wb'))
    print("amount of ships: " + str(len(selectedlist)))
    print("total costs: " + str(calculatetotal(selectedlist)))
    # return the found solution in dictionary form
    return picklename
