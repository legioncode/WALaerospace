from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import depthmoves
from code.helperfunctions.assign import assign, calculatepackages, returnLastParcel, solution, undomove


def depth (shiplist, cargolist):
    sol = (0 , {})
    depth = 0
    kids = depthmoves(shiplist, cargolist,depth)
    movelist = []

    while kids != []:
        move = kids.pop(0)
        assign(move[0], move[1])
        movelist.append(move)
        cargolist.remove(move[1])
        depth += 1
        newkids = depthmoves(shiplist, cargolist, depth)

        if newkids != []:
            kids = newkids + kids

        else:
            if len(movelist) > sol[0]:
                sol = (len(movelist), solution(shiplist))

            lastmove = movelist[-1]
            nextmove  = kids[0]
            while lastmove[2] >= nextmove[2]:
                undomove(lastmove[0], lastmove[1])
                cargolist.append(lastmove[1])
                movelist.pop(-1)
                lastmove = movelist[-1]

    print(sol[0])
    sdict = sol[1]
    for i in sdict.keys():
        print(i.name)
        print(i.payload)
        print(i.volume)
