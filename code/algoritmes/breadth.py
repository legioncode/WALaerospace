from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.classes.packinglist import Packinglist
from code.helperfunctions.possiblemoves import possiblemovesA, checkmove
#from code.helperfunctions.assign import assign, undomove
import copy

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

def Breadth(shiplist, parcellist):
    # compute amount of moves optimal solution
    maxmoves = len(parcellist)

    # initialize an empty queue
    queue = []
    counter = len(queue)
    object = Packinglist(counter, [])
    queue.append(object)
    solution = queue[0]

    # while there's customers in queue
    while len(queue) != 0:

        # remove and give to me the first customer in line
        first = queue.pop(0)

        # perform the moves this customer has with him already
        for i in range(len(first.moves)):
            AssignBreadth(shiplist, first.moves[i][0], first.moves[i][1])
            for parcel in parcellist:
                if first.moves[i][1].id == parcel.id:
                    parcellist.remove(parcel)

        # compute this customer's children
        kids = possiblemovesA(shiplist, parcellist)

        # create a packinglist object for each child
        for move in kids:
            base = copy.deepcopy(first.moves)
            base.append(move)
            kid = Packinglist(counter, base)
            counter += 1

            # if child appends more parcels than the current best solution, make it the cbs
            if len(kid.moves) > len(solution.moves):
                solution = kid
                queue.append(kid)

            # if this child is an optimal solution, stop
            if len(kid.moves) == maxmoves:
                break

            # else, put the child in the back of the queue
            else:
                queue.append(kid)

        for i in range(len(first.moves)):
            UndoBreadth(shiplist, first.moves[i][0], first.moves[i][1])
            parcellist.append(first.moves[i][1])

    print("done")
    print(f"solution = {solution} with id {solution.id} with {len(solution.moves)} moves in it")
    print(f"these moves are {solution.moves}")
    for move in solution.moves:
        if checkmove(move[1], move[0]):
            AssignBreadth(shiplist, move[0], move[1])
    for ship in shiplist:
        print(f"ship {ship.name} carries {len(ship.assigned)} packages")
    return shiplist
