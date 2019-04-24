from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import possiblemovesA
from code.helperfunctions.assign import assign, calculatepackages, returnLastParcel, solution, undomove

def depth(shiplist, cargolist):

    sol = (0, {})
    children = possiblemovesA(shiplist, cargolist)
    movelist = []
    nParcels = len(cargolist)

    c = 0
    while children != []:
        c += 1
        if c == 1000:
            break
        move = children.pop(0)
        assign(move[0], move[1])
        cargolist.remove(move[1])
        movelist.append(move)
        nextlist = possiblemovesA(shiplist, cargolist)

        if len(movelist) > sol[0]:
            sol = (len(movelist), solution(shiplist))
        if len(nextlist) > 0:
            children = nextlist + children
        else:
            checkmove = children[0]
            while checkmove[1] not in cargolist:
                lastmove = movelist.pop(-1)
                undomove(lastmove[0], lastmove[1])
                cargolist = [lastmove[1]] + cargolist


    print('answer ='+ str(sol[0]))
    totalN = 0
    for i in sol[1]:
        totalN += len(i.assigned)
        #print(i.name)
        #print('assigned mass: ' + str(sum([x.mass for x in i.assigned])))
        #print('assigned volume: ' + str(sum([x.size for x in i.assigned])))
        #print('---------------------')
    print('total assigned: ' + str(totalN))
