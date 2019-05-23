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
import random


def maersk(shiplist, parcellist):
    '''Maersk is is a greedy algorithm for problem D. It takes two arguments.
    The first argument is a list of spaceship objects to use, the second a list
    of cargo objects to assign.

    The function is used to Solve problem D and is designed for very large
    cargolists and  a list of spaceships that can be used without constraints.

    Maersk will loop through the parcellist and will do the following for each
    cargo object. It calculates the optimal space ship to assign the parcel to
    based on matching the parcels mass to volume ratio and the spaceships
    carrymass to carryvolume ratio. If there is an ship of that class in the
    current fleet with room it will assign the parcel to that ship, otherwise
    it will add another spaceship of this class to the current fleet.

    The algorithm is a greedy constructive algoritm with the mass to volume
    match as it's heuristic.
     '''
    # the list that represents the current fleet
    selectedlist = []
    timelist = shiplist
    countrylist = [i.nation for i in shiplist]
    print(" you're running the greedy algorithm for problem D you can now \
            select some options to run it: ")
    bool = input("you can choose to remove the spaceships from a country \
    to improve the solution. type yes if you want this, any other input will \
    result in a normal run ")
    bool = bool.lower()
    if bool == 'yes':
        country = input("what country do you want to remove? options: Russia, \
        Europe, USA, China, Japan. (Removing USA gives best solution) ")
        if country in countrylist:
            for i in timelist:
                if i.nation == country:
                    print('country removed')
                    shiplist.remove(i)

    # the list that gets the MW from all spaceship classes
    shipmv = [x.mv for x in shiplist]
    for i in parcellist:
        bool = False
        shipname = calculateoptimal(i, shiplist)
        namelist = [i.name for i in selectedlist]

        if shipname.name not in namelist:
            spacecraft = Spacecraft(shipname.name, shipname.nation,
                                    shipname.payload, shipname.volume,
                                    shipname.mass, shipname.basecost,
                                    shipname.ftw)
            assign(spacecraft, i)
            selectedlist.append(spacecraft)

        elif shipname.name in namelist:
            indexes = []
            for z in range(len(namelist)):
                if namelist[z] == shipname.name:
                    indexes.append(z)

            for y in indexes:
                if checkmove(i, selectedlist[z]):
                    if bool is False:
                        assign(selectedlist[z], i)

                    bool = True
                    break

            if bool is False:
                spacecraft = Spacecraft(shipname.name, shipname.nation,
                                        shipname.payload, shipname.volume,
                                        shipname.mass, shipname.basecost,
                                        shipname.ftw)
                assign(spacecraft, i)
                selectedlist.append(spacecraft)

    print("amount of ships: " + str(len(selectedlist)))
    print("total costs: " + str(calculatetotal(selectedlist)))
    # return the found solution in dict form to be able to work with later
    return solution(selectedlist)
