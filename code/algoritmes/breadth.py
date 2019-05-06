from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.classes.packinglist import Packinglist
from code.helperfunctions.possiblemoves import possiblemovesA
from code.helperfunctions.assign import assign

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

    # while there's customers in queue
    ronde = 0
    while len(queue) != 0:
    #for i in range(3):
        ronde += 1
        print(f"{ronde}")

        # remove and give to me the first customer in line
        firststack = queue.pop(0)

        # perform the moves this customer has with him already
        worklist = list(parcellist)
        #print(f"length moves firststack = {len(firststack.moves)}")
        for i in range(len(firststack.moves)):
            #for i in range(len(worklist)):
            #    print(f"worklist = {worklist[i].id}")
            #print(f"id of parcel = {firststack.moves[i][1].id}")
            assign(firststack.moves[i][0], firststack.moves[i][1])
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

            # else, put the child in the back of the queue
            else:
                queue.append(newcustomer)
    print(f"done")
