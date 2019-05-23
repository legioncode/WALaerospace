import copy


def assign(ship, parcel):
    """Takes in a ship and a parcel, assigns the parcel to the ship."""
    worklist = ship.assigned
    worklist.append(parcel)
    ship.assigned = worklist
    ship.volume = ship.volume - parcel.size
    ship.payload = ship.payload - parcel.mass
    parcel.ship = ship
    ship.ratio()


def undomove(ship, parcel):
    """Takes in a ship and a parcel, unassigns the parcel to the ship."""
    if parcel in ship.assigned:
        newassign = ship.assigned.remove(parcel)
        ship.volume = ship.volume + parcel.size
        ship.payload = ship.payload + parcel.mass
        parcel.ship = None


def solution(shiplist):
    """Takes in shiplist with a solution, and turns it into a dictionary of
    ship:packages pairs."""
    solutiondict = {}
    for i in shiplist:
        solutiondict[i] = i.assigned
    return solutiondict


def updatemv(shiplist):
    """Takes in a shiplist and updates the mass-volume ratios of the
    ships in it."""
    return [x.mv for x in shiplist]


def clearships(shiplist):
    """Takes in a shiplist and restores it to its initial state."""
    for i in shiplist:
        i.assigned = []
        i.payload = copy.deepcopy(i.firstpayload)
        i.volume = copy.deepcopy(i.firstvolume)
        i.mv = i.payload / float(i.volume)


def assignfromdict(shipdict):
    """Takes in a dictionary of a solution, and assigns the packages to their
    ships."""
    for i in shipdict.keys():
        shipdict[i].assigned = shipdict[i]


def calculatetotal(shiplist):
    """Takes in a shiplist, calculates and returns its total cost."""
    cost = 0
    for i in shiplist:
        cost += i.cost
    return cost


def loadstate(solution, shiplist):
    """Takes in a dictionary of a solution and a shiplist, and performs
    the moves of the dictionary on the shiplist."""
    for i in solution.keys():
        for x in shiplist:
            if i.name == x.name:
                x.assigned = solution[i]
                x.ratio()


def calculatepackages(shiplist):
    """Takes in a shiplist of a solution, calculates and returns the amount of
    assigned packages."""
    return sum(len(i.assigned) for i in shiplist)


def returnLastParcel(ship):
    """Takes in a ship, removes and returns the last assigned parcel."""
    parcel = ship.assigned.pop(-1)
    ship.volume = ship.volume + parcel.size
    ship.payload = ship.payload + parcel.mass
    ship.ratio()
    return parcel

def calculateoptimal(parcel, shiplist):
    ''' calculate optimal calculates the optimal matches spaceship out of
        a list of ships and returns that ship. It takes in two arguments:
        a cargo object and a list of shipobjects '''
    defaultship = (0, 400)
    shipmv = [x.mv for x in shiplist]
    for z in range(len(shipmv)):
        difference = max(shipmv[z], parcel.mv) - min(shipmv[z], parcel.mv)
        if difference < defaultship[1]:
            defaultship = (z, difference)

    return shiplist[defaultship[0]]
