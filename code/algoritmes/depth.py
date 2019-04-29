from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import possiblemovesA
from code.helperfunctions.assign import assign, calculatepackages, returnLastParcel, solution, undomove


def depth (shiplist, cargolist):
    sol = (0 , {})
    kids = possiblemovesA(shiplist, cargolist)
    movelist = []


    while kids != []:
        move = kids.pop(0)
        assign(move[0], move[1])
        movelist.append(move)
        cargolist.remove(move[1])
        newkids = possiblemovesA(shiplist, cargolist)

        if newkids != []:
            kids = newkids + kids

        else:
            if len(movelist) > sol[0]:
                sol = (len(movelist), solution(shiplist))

            lastmove = movelist.pop(-1)
            undomove(lastmove[0], lastmove[1])
            cargolist.append(lastmove[1])
            nextmove  = kids[0]

            while nextmove[1] not in cargolist:

    print(sol[0])
