from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.classes.packinglist import Packinglist
from code.helperfunctions.possiblemoves import possiblemovesA, checkmove
from code.helperfunctions.assign import calculatetotal
import copy
import pickle

def GetInput(shiplist, parcellist):
    maxamount = len(possiblemovesA(shiplist, parcellist))
    while True:
        w = int(input("Choose a beamwidth: "))
        if w >= 1 and w <= maxamount:
            break
        else:
            print(f"Beamwidth should be between 1 and {maxamount}")
    return w

def AssignBreadth(shiplist, parcellist, spacecraft, parcel):
    for ship in shiplist:
        if spacecraft.name == ship.name:
            for package in parcellist:
                if package.id == parcel.id:
                    ship.assigned.append(package)
                    ship.volume = ship.volume - package.size
                    ship.payload = ship.payload - package.mass
                    parcellist.remove(package)
                    ship.ratio()

def UndoBreadth(shiplist, parcellist, spacecraft, parcel):
    for ship in shiplist:
        if spacecraft.name == ship.name:
            for package in ship.assigned:
                if package.id == parcel.id:
                    ship.assigned.remove(package)
                    ship.volume = ship.volume + package.size
                    ship.payload = ship.payload + package.mass
                    parcellist.append(package)
                    ship.ratio()

def Beam(shiplist, parcellist):
    # get beamwidth
    beamwidth = GetInput(shiplist, parcellist)

    # compute amount of moves optimal solution
    maxmoves = len(parcellist)

    # initialize queue with empty Parcellist object
    queue = []
    solutions = []
    bestsolution = None
    counter = len(queue)
    object = Packinglist(counter, [], 0)
    queue.append(object)
    solutions.append(object)
    kidlist = []

    # while there's objects in queue
    while len(queue) != 0:
        quelength = len(queue)
        for i in range(quelength):
            # remove and get the first object of queue
            first = queue.pop(0)

            # perform the moves this object has with him already
            for j in range(len(first.moves)):
                AssignBreadth(shiplist, parcellist, first.moves[j][0], first.moves[j][1])

            # compute this object's children
            kids = possiblemovesA(shiplist, parcellist)

            # create a packinglist object for each child
            for move in kids:
                base = copy.deepcopy(first.moves)
                base.append(move)
                ratiodiff = abs(1 - (move[0].mv / move[1].mv))
                kid = Packinglist(counter, base, ratiodiff)
                counter += 1
                kidlist.append(kid)

            for k in range(len(first.moves)):
                UndoBreadth(shiplist, parcellist, first.moves[k][0], first.moves[k][1])

        if len(kidlist) == 0:
            break

        # sort kidlist ascending based on weight
        sortedkids = sorted(kidlist, key=lambda packinglist: packinglist.ratiodiff, reverse=False)

        # choose beamwidth amount of children you want to keep
        for i in range(beamwidth):
            if i < len(sortedkids):
                queue.append(sortedkids[i])

                # if child appends more parcels than the current best solution, make it the cbs
                for sol in solutions:
                    if len(sortedkids[i].moves) >= len(sol.moves):
                        solutions.append(sortedkids[i])
                        break

                for sol in solutions:
                    if len(sortedkids[i].moves) > len(sol.moves):
                        solutions.remove(sol)
            else:
                break

        kidlist.clear()


    print(f"shiplist before checking a solution")
    for ship in shiplist:
        print(f"ship {ship.name} carries {len(ship.assigned)} packages and has {ship.payload} kg left and {ship.volume} m3 left")

    for solution in solutions:
        for move in solution.moves:
            AssignBreadth(shiplist, parcellist, move[0], move[1])
        cost = calculatetotal(shiplist)
        solution.cost = cost
        for move in solution.moves:
            UndoBreadth(shiplist, parcellist, move[0], move[1])
        print(f"shiplist after checking a solution")
        for ship in shiplist:
            print(f"ship {ship.name} carries {len(ship.assigned)} packages and has {ship.payload} kg left and {ship.volume} m3 left")

    sortedsolutions = sorted(solutions, key=lambda packinglist: packinglist.cost, reverse=False)
    bestsolution = sortedsolutions[0]
    pickle.dump(bestsolution, open('beamsolution.p', 'wb'))
    print(f"shiplist before assignment")
    for ship in shiplist:
        print(f"ship {ship.name} carries {len(ship.assigned)} packages and has {ship.payload} kg left and {ship.volume} m3 left")
    for move in bestsolution.moves:
        if checkmove(move[1], move[0]):
            AssignBreadth(shiplist, parcellist, move[0], move[1])
    print(f"bestsolution has a length of {len(bestsolution.moves)} and costs {bestsolution.cost}")
    for ship in shiplist:
        print(f"ship {ship.name} carries {len(ship.assigned)} packages and has {ship.payload} kg left and {ship.volume} m3 left")
    return shiplist
