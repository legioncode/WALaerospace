from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.classes.packinglist import Packinglist
from code.helperfunctions.possiblemoves import possiblemovesA
from code.helperfunctions.assign import assign, undomove
import copy

def Breadth(shiplist, parcellist):
    # compute amount of moves optimal solution
    maxmoves = len(parcellist)

    # initialize an empty queue
    queue = []

    # compute first depth of nodes to fill queue with
    posmoves = possiblemovesA(shiplist, parcellist)

    # create a Packinglist object voor each move, and add to queue
    for i in range(len(posmoves)):
        object = Packinglist(i, [posmoves[i]])
        queue.append(object)

    # keep track of amount of customers in queue
    counter = len(queue)

    # keep track of best Packinglist uptill now
    solution = queue[0]

    # while there's customers in queue
    while len(queue) != 0:

        # remove and give to me the first customer in line
        first = queue.pop(0)
        #for parcel in parcellist:
        #    print(f"parcellist before: {parcel.id}")

        # perform the moves this customer has with him already
        for i in range(len(first.moves)):
            assign(first.moves[i][0], first.moves[i][1])
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
            undomove(first.moves[i][0], first.moves[i][1])
            parcellist.append(first.moves[i][1])

        #for parcel in parcellist:
            #print(f"parcellist after: {parcel.id}")

    print(f"solution = {solution}")
    print(f"solutionid = {solution.id}")
    print(f"solution moves = {len(solution.moves)}")
    for move in solution.moves:
        print(f"{move[1].id} in {move[0].name}")
    # perform the moves this customer has with him already
    for i in range(len(solution.moves)):
        assign(solution.moves[i][0], solution.moves[i][1])
        for parcel in parcellist:
            if solution.moves[i][1].id == parcel.id:
                parcellist.remove(parcel)
    for ship in shiplist:
        print(f"ship {ship.name} carries {len(ship.assigned)} packages")
    print(f"parcellist has {len(parcellist)} packages")
