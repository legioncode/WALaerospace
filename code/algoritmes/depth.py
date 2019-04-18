from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import possiblemovesA
from code.helperfunctions.assign import assign, calculatepackages, returnLastParcel, solution, undomove

def depth(shiplist, cargolist):
    sol = (0, {})
    children = possiblemovesA(shiplist, cargolist)
    nParcels = len(cargolist)
    movelist = []

    while children != []:
        move = children.pop(0)
        assign(move[0], move[1])
        cargolist.remove(move[1])
        newkids = possiblemovesA(shiplist, cargolist)

        if len(newkids) == 0:
            undomove(move[0], move[1])
            lastmove = movelist.pop(-1)
            cargolist.append(lastmove[1])
            if len(movelist) > sol[0]:
                sol = (len(movelist), solution(shiplist))
                if len(movelist) == nParcels:
                    print('hoi')
                    break
        else:
            movelist.append(move)
            children = newkids + children


    print('answer ='+ str(sol[0]))
    for i in sol[1]:
        print(i.payload)
        print(i.volume)
        print(len(i.assigned))
        print('---------------------')
