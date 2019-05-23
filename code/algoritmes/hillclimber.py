from code.helperfunctions.assign import assign
from code.helperfunctions.assign import calculatepackages
from code.helperfunctions.assign import calculatetotal
from code.helperfunctions.assign import loadstate
from code.helperfunctions.assign import solution
from code.helperfunctions.assign import undomove
from code.algoritmes.dhl import dhl
from code.helperfunctions.possiblemoves import checkmove
import pickle
import random


def hillclimber(shiplist, parcellist):
    max = int(input("How many times do you want to run this algorithm: "))
    while max == "":
        max = int(input("How many times do you want to run this algorithm: "))
    startcost = calculatetotal(shiplist)
    startpackages = calculatepackages(shiplist)
    startsolution = solution(shiplist)

    for c in range(max):
        assignedparcellist = [e for i in shiplist for e in i.assigned]
        remainparcellist = [i for i in parcellist if i not in
                            assignedparcellist]
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

    filename = input("Please name how you want to save this solution: ")
    while filename == "":
        filename = input("Please name how you want to save this solution: ")
    picklename = str(f"results/Newsolutions/{filename}.p")
    pickle.dump(shiplist, open(picklename, 'wb'))
    return picklename
