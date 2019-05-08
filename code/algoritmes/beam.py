from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.classes.packinglist import Packinglist
from code.helperfunctions.possiblemoves import possiblemovesA, checkmove
#from code.helperfunctions.assign import assign, undomove
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

def AssignBreadth(shiplist, spacecraft, parcel):
    for ship in shiplist:
        if spacecraft.name == ship.name:
            ship.assigned.append(parcel)
            ship.volume = ship.volume - parcel.size
            ship.payload = ship.payload - parcel.mass
            parcel.ship = ship

def UndoBreadth(shiplist, spacecraft, parcel):
    for ship in shiplist:
        if spacecraft.name == ship.name:
            ship.assigned.remove(parcel)
            ship.volume = ship.volume + parcel.size
            ship.payload = ship.payload + parcel.mass
            parcel.ship = None

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
        print(f"length queue = {len(queue)}")
        print("newround")
        for object in queue:
            # remove and get the first object of queue
            first = queue.pop(0)

            # perform the moves this object has with him already
            for i in range(len(first.moves)):
                AssignBreadth(shiplist, first.moves[i][0], first.moves[i][1])
                for parcel in parcellist:
                    if first.moves[i][1].id == parcel.id:
                        parcellist.remove(parcel)

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
                UndoBreadth(shiplist, first.moves[i][0], first.moves[i][1])
                parcellist.append(first.moves[i][1])
            break

        # sort kidlist ascending based on weight
        sortedkids = sorted(kidlist, key=lambda packinglist: packinglist.weight, reverse=False)

        # choose beamwidth amount of children you want to keep
        for i in range(beamwidth):
            print("object appended to queue")
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
            UndoBreadth(shiplist, first.moves[i][0], first.moves[i][1])
            parcellist.append(first.moves[i][1])

    #for space in shiplist:
    #    print(f"spacecraft {space.name} carries {len(space.assigned)} packages")
    #print("------------------------")
    #print(f"solution is {solution} with id {solution.id} and {len(solution.moves)} moves")
    #for move in solution.moves:
    #    print(f"parcel {move[1].id} goes in {move[0].name}")
    print("shiplist after beamsearch = ")
    for ship in shiplist:
        ship.assigned.clear()
        print(f"ship {ship.name} carries {len(ship.assigned)} packages")
    print("parcellist after beamsearch = ")
    for parcel in parcellist:
        print(f"parcel {parcel.id}")
    print("_________________________________________________________")
    return solution

def CheckSol(shiplist, parcellist, solution):
    for ship in shiplist:
        ship.assigned.clear()
        print(f"ship {ship.name} carries {len(ship.assigned)} packages")
    print("_________________________________________________________")
    for move in solution.moves:
        if checkmove(move[1], move[0]):
            AssignBreadth(shiplist, move[0], move[1])
    for ship in shiplist:
        print(f"ship {ship.name} carries {len(ship.assigned)} packages")
