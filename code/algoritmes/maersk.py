import numpy as np
import pandas as pd
import random
from code.helperfunctions.assign import assign, loadstate, clearships, solution
from code.helperfunctions.possiblemoves import checkmove
from code.classes.spacecraft import Spacecraft

def maersk(shiplist, parcellist, constraint):
    selectedlist = []
    fulllist = []
    shipmv = [x.mv for x in shiplist]
    c = 0

    for i in parcellist:
        bool = False
        defaultship = (0, 400)

        for z in range(len(shipmv)):
            difference = max(shipmv[z], i.mv) - min(shipmv[z], i.mv)
            if difference < defaultship[1]:
                defaultship = (z, difference)

        shipname = shiplist[defaultship[0]]
        namelist = [i.name for i in selectedlist]

        if shipname.name not in namelist:
            spacecraft = Spacecraft(shipname.name, shipname.nation, shipname.payload,
                                    shipname.volume, shipname.mass, shipname.basecost, shipname.ftw)
            assign(spacecraft, i)
            c += 1
            selectedlist.append(spacecraft)

        elif shipname.name in namelist:
            indexes = []
            for z in range(len(namelist)):
                if namelist[z] == shipname.name:
                    indexes.append(z)

            for y in indexes:
                if checkmove(i, selectedlist[z]):
                    if bool == False:
                        assign(selectedlist[z], i)
                        c += 1

                    bool = True
                    break

            if bool == False:
                spacecraft = Spacecraft(shipname.name, shipname.nation, shipname.payload,
                                        shipname.volume, shipname.mass, shipname.basecost, shipname.ftw)
                assign(spacecraft, i)
                c += 1
                selectedlist.append(spacecraft)


    return solution(selectedlist)
