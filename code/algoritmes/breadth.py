from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
# maak een klasse "packing list (PL)" oid
    # id(int), packed(list)
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

def Breadth(shiplist, parcellist):
    # initialize an empty queue
    queue = []

    # compute first depth of nodes to fill queue with
    posmoves = possiblemovesA(shiplist, parcellist)

    # create a Packinglist object voor each move, and add to queue
    for i in range(len(posmoves)):
        stack = Packinglist(i, [posmoves[i]])
        queue.append(stack)

    # keep track of amount of customers in queue
    counter = len(queue)

    # keep track of best Packinglist uptill now
    currentbestsolution = queue[0]
    print(f"currentbestsolution = {currentbestsolution}")

    # while there's customers in queue
    # while len(queue) != 0:
    for i in range(5):
        print(f"i = {i}")

        # remove and give to me the first customer in line
        print(f"length of que is {len(queue)}")
        firststack = queue.pop(0)
        print(f"current stack working on = {firststack.id} with {len(firststack.moves)} moves in it")

        # (temporarily) perform the moves this customer has with him already
        for i in range(len(firststack.moves)):
            temporarilyAssign(firststack.moves[i][0], firststack.moves[0][1])
            print(f"the id of the current parcel = {firststack.moves[0][1].id}")
            worklist = parcellist
            #for item in worklist:
                #print(f"this item in worklist has id: {item.id}")
            worklist.remove(firststack.moves[0][1])

            # compute this customer's children, and add them to the queue
            posmoves = possiblemovesA(shiplist, worklist)
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

                # else, put the child in the back of the queue
                else:
                    queue.append(newcustomer)
