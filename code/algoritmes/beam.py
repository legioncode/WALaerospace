from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.classes.packinglist import Packinglist
#from code.helperfunctions.possiblemoves import possiblemovesA

def temporarilyAssign(ship, parcel):
    worklist = ship.assigned
    worklist.append(parcel)
    ship.assigned = worklist
    ship.volume = ship.volume - parcel.size
    ship.payload = ship.payload - parcel.mass
    parcel.ship = ship

def possiblemovesA(shiplist, parcellist):
    possiblemoves = []
    for i in parcellist:
        for x in shiplist:
            if i.mass <= x.payload and i.size <= x.volume:
                possiblemoves.append((x, i))
    return possiblemoves

def Beam(shiplist, parcellist):
    beamwidth = 4
    # initialize an empty queue
    queue = []
    waitinglist = []

    # compute first depth of nodes to fill queue with
    posmoves = possiblemovesA(shiplist, parcellist)

    # create a Packinglist object voor each move, and add to queue
    for i in range(len(posmoves)):
        stack = Packinglist(i, [posmoves[i]])
        waitinglist.append(stack)

    sortedstack = sorted(waitinglist, key=lambda packinglist: packinglist.id, reverse=True)

    for i in range(beamwidth):
        candidate = sortedstack[i]
        queue.append(candidate)

    # keep track of amount of customers in queue
    counter = len(queue)

    # keep track of best Packinglist uptill now
    currentbestsolution = queue[0]

    # while there's customers in queue
    while len(queue) != 0:
        kidlist = []

        for i in range(beamwidth):
            # remove and give to me the first customer in line
            firststack = queue.pop(0)

            # (temporarily) perform the moves this customer has with him already
            worklist = list(parcellist)
            for i in range(len(firststack.moves)):
                temporarilyAssign(firststack.moves[i][0], firststack.moves[i][1])
                worklist.remove(firststack.moves[0][1])

            # compute this customer's children
            posmoves = possiblemovesA(shiplist, worklist)

            # create a packinglist object for each child
            for move in posmoves:
                move = [move]
                updatedmoves = [firststack.moves + move]
                newcustomer = Packinglist(counter, [updatedmoves])
                counter += 1

                # if child appends more parcels than the current best solution, make it the cbs
                if len(newcustomer.moves) > len(currentbestsolution.moves):
                    currentbestsolution = newcustomer

                # if this child is an optimal solution, stop
                if len(newcustomer.moves) == 100:
                    break

                # else, put the child in kidlist
                else:
                    kidlist.append(newcustomer)

        # sort the kidlist
        sortedkids = sorted(kidlist, key=lambda packinglist: packinglist.id, reverse=True)
        # put 4 in the queue, forget about the rest
        for i in range(beamwidth):
            candidate = sortedkids[i]
            queue.append(candidate)


    print(f"done")
