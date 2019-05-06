from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import depthmoves
from code.helperfunctions.assign import assign, undomove

def Breadth2(shiplist, parcellist):
    sol = (0, 0, {})
    depth = 0
    queue = depthmoves(shiplist, cargolist, depth)
    movelist = []

    while queue != []
        first = queue.pop[0]
        assign(first[0], first[1])
        cargolist.remove(first[1])
        depth = first[3] + 1
        newkids = depthmoves(shiplist, cargolist, depth)
        if newkids != []:
            queue = queue + newkids
            undomove(first[0], first[1])
            cargolist.append(first[1])
        else:
            if sol[0] == len(movelist):
                if sol[1] > calculatetotal(shiplist):
                    sol = (len(movelist), calculatetotal(shiplist), solution(shiplist))
            elif sol[0] < len(movelist):
                sol = (len(movelist), calculatetotal(shiplist), solution(shiplist))

            undomove(first[0], first[1])
            cargolist.append(first[1])
