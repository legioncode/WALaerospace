from code.classes.cargo import Cargo
from code.classes.packinglist import Packinglist
from code.classes.spacecraft import Spacecraft
import copy
from code.helperfunctions.assign import calculatetotal
from code.helperfunctions.possiblemoves import checkmove
from code.helperfunctions.possiblemoves import possiblemovesA
import pickle


def GetInput(shiplist, parcellist):
    """Takes as input a clear shiplist and parcellist. Prompts the user for a
    beamwidth and validates this. Returns the beamwidth"""
    maxamount = len(possiblemovesA(shiplist, parcellist))
    while True:
        w = int(input("Choose a beamwidth: "))
        if w >= 1 and w <= maxamount:
            break
        else:
            print(f"Beamwidth should be between 1 and {maxamount}")
    return w


def assignBeam(shiplist, parcellist, spacecraft, parcel):
    """Takes as input the current ship- and parcellist, and the ship and parcel
    involved in the move to be performed. Returns the updated ship- and
    parcellist"""
    for ship in shiplist:
        if spacecraft.name == ship.name:
            for package in parcellist:
                if package.id == parcel.id:
                    ship.assigned.append(package)
                    ship.volume = ship.volume - package.size
                    ship.payload = ship.payload - package.mass
                    parcellist.remove(package)
                    ship.ratio()
    return shiplist, parcellist


def undoBeam(shiplist, parcellist, spacecraft, parcel):
    """Takes as input the current ship- and parcellist, and the ship and parcel
    involved in the move to be undone. Returns the updated ship- and
    parcellist"""
    for ship in shiplist:
        if spacecraft.name == ship.name:
            for package in ship.assigned:
                if package.id == parcel.id:
                    ship.assigned.remove(package)
                    ship.volume = ship.volume + package.size
                    ship.payload = ship.payload + package.mass
                    parcellist.append(package)
                    ship.ratio()
    return shiplist, parcellist


def Beam(shiplist, parcellist):
    """Takes as input a clear ship- and parcellist. Performs a beamsearch of
    width n, based on correspondence of mass-volume ratio. Writes the shiplist
    of the best found solution to a pickle file the filename of which is
    returned ."""

    print(f"Running this beam algorithm might take a while depending on the chosen beamwidth. If you're looking for a fast result advice a beamwidth between 2-5.")
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

            # get first object from queue to work with
            first = queue.pop(0)

            # perform the moves this object has with him already
            for j in range(len(first.moves)):
                shiplist, parcellist = assignBeam(
                    shiplist, parcellist, first.moves[j][0], first.moves[j][1])

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
                shiplist, parcellist = undoBeam(
                    shiplist, parcellist, first.moves[k][0], first.moves[k][1])

        if len(kidlist) == 0:
            break

        # sort kidlist ascending based on mass-volume ratio difference between
        # parcel and ship of last appended move
        sortedkids = sorted(kidlist, key=lambda packinglist:
                            packinglist.ratiodiff, reverse=False)

        # choose beamwidth amount of children you want to keep
        for i in range(beamwidth):
            if i < len(sortedkids):
                queue.append(sortedkids[i])

                # if child appends more parcels than the current best solution,
                # make it the current best solution
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

    # calculate cost of each solution
    for solution in solutions:
        for move in solution.moves:
            shiplist, parcellist = assignBeam(shiplist, parcellist, move[0],
                                              move[1])
        cost = calculatetotal(shiplist)
        solution.cost = cost
        for move in solution.moves:
            shiplist, parcellist = undoBeam(shiplist, parcellist, move[0],
                                            move[1])

    # sort solutions based on cost, the cheapest solution will be saved
    sortedsolutions = sorted(solutions, key=lambda packinglist:
                             packinglist.cost, reverse=False)
    bestsolution = sortedsolutions[0]

    # make the shiplist for the best solution
    for move in bestsolution.moves:
        if checkmove(move[1], move[0]):
            shiplist, parcellist = assignBeam(shiplist, parcellist, move[0],
                                              move[1])

    # save the best solution
    filename = input("Please name how you want to save this solution: ")
    while filename == "":
        filename = input("Please name how you want to save this solution: ")
    picklename = str(f"results/Newsolutions/{filename}.p")
    pickle.dump(shiplist, open(picklename, 'wb'))
    return picklename
