from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.classes.packinglist import Packinglist
from code.helperfunctions.possiblemoves import possiblemovesA, checkmove
import copy

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

def UndoBreadth(shiplist, parcellist, spacecraft, parcel):
    for ship in shiplist:
        if spacecraft.name == ship.name:
            for package in ship.assigned:
                if package.id == parcel.id:
                    ship.assigned.remove(package)
                    ship.volume = ship.volume + package.size
                    ship.payload = ship.payload + package.mass
                    parcellist.append(package)

def Beam(shiplist, parcellist):
    # get beamwidth
    beamwidth = GetInput(shiplist, parcellist)

    # compute amount of moves optimal solution
    maxmoves = len(parcellist)

    # initialize queue with empty Parcellist object
    queue = []
    counter = len(queue)
    object = Packinglist(counter, [])
    queue.append(object)
    solution = queue[0]
    kidlist = []

    # while there's objects in queue
    while len(queue) != 0:
        for object in queue:
            # remove and get the first object of queue
            first = queue.pop(0)

            # perform the moves this object has with him already
            for i in range(len(first.moves)):
                AssignBreadth(shiplist, parcellist, first.moves[i][0], first.moves[i][1])

            # compute this object's children
            kids = possiblemovesA(shiplist, parcellist)

            # create a packinglist object for each child
            for move in kids:
                base = copy.deepcopy(first.moves)
                base.append(move)
                kid = Packinglist(counter, base)
                counter += 1
                kidlist.append(kid)

        if len(kidlist) == 0:
            for i in range(len(first.moves)):
                UndoBreadth(shiplist, parcellist, first.moves[i][0], first.moves[i][1])
            break

        # sort kidlist ascending based on weight
        sortedkids = sorted(kidlist, key=lambda packinglist: packinglist.weight, reverse=False)

        # choose beamwidth amount of children you want to keep
        for i in range(beamwidth):
            queue.append(sortedkids[i])

            # if child appends more parcels than the current best solution, make it the cbs
            if len(sortedkids[i].moves) > len(solution.moves):
                solution = sortedkids[i]

            # if this child is an optimal solution, stop
            if len(sortedkids[i].moves) == maxmoves:
                break

        # undo the moves
        kidlist.clear()
        for i in range(len(first.moves)):
            UndoBreadth(shiplist, parcellist, first.moves[i][0], first.moves[i][1])

    return solution

def CheckSol(shiplist, parcellist, solution):
    print(f"shiplist at begin of checksol")
    for ship in shiplist:
        #ship.assigned.clear()
        print(f"ship {ship.name} carries {len(ship.assigned)} packages has {ship.payload} kg and {ship.volume}m3 left")
    print("_________________________________________________________")
    for move in solution.moves:
        print(f"package {move[1].id} weights {move[1].mass} kg and is {move[1].size} m3 and should go in {move[0].name}")
        if checkmove(move[1], move[0]):
            print("valid move")
            AssignBreadth(shiplist, parcellist, move[0], move[1])
        else:
            print("invalid move")
    for ship in shiplist:
        print(f"ship {ship.name} carries {len(ship.assigned)} packages has {ship.payload} kg and {ship.volume}m3 left")
