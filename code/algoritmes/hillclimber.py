from code.helperfunctions.assign import calculatetotal, calculatepackages, undomove, solution, assign, loadstate
from code.helperfunctions.possiblemoves import checkmove
from code.algoritmes.flessenpost import flessenpost
from code.algoritmes.dhl import dhl
import random
import pickle


def hillclimber(shiplist, parcellist):
    startcost = calculatetotal(shiplist)
    startpackages = calculatepackages(shiplist)
    startsolution = solution(shiplist)
    assignedparcellist = [e for i in shiplist for e in i.assigned]
    remainparcellist = [i for i in parcellist if i not in assignedparcellist]
    wholeparcellist = assignedparcellist + remainparcellist

    for c in range(10000000):
        ship1 = shiplist[random.randint(0, len(shiplist) - 1)]
        ship2 = shiplist[random.randint(0, len(shiplist) - 1)]
        while ship1 == ship2:
            ship2 = shiplist[random.randint(0, len(shiplist) - 1)]
        package1 = ship1.assigned[random.randint(0, len(ship1.assigned) - 1)]
        package2 = ship2.assigned[random.randint(0, len(ship2.assigned) - 1)]
        undomove(ship1, package1)
        undomove(ship2, package2)

        if checkmove(package2, ship1) and checkmove(package1, ship2):
            assign(ship1, package2)
            assign(ship2, package1)
            shiplist = dhl(shiplist, remainparcellist)
            if startcost <= calculatetotal(shiplist):
                startcost = calculatetotal(shiplist)
                startsolution = solution(shiplist)
            if startpackages < calculatepackages(shiplist):
                startcost <= calculatetotal(shiplist)
                startpackages = calculatepackages(shiplist)
                startsolution = solution(shiplist)
        else:
            assign(ship1, package1)
            assign(ship2, package2)
        loadstate(startsolution, shiplist)


    pickle.dump(shiplist, open('toppervandeweek2.p', 'wb'))
    return startpackages
