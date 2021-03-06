from code.helperfunctions.assign import assign
from code.helperfunctions.assign import solution
from code.helperfunctions.assign import calculateoptimal
from code.helperfunctions.assign import calculatetotal
from code.helperfunctions.possiblemoves import checkmove
from code.helperfunctions.possiblemoves import possiblemovesA
from code.classes.spacecraft import Spacecraft
import pickle


def maersk(shiplist, parcellist):
    '''Maersk is is a greedy algorithm for problem D. It takes two arguments.
    The first argument is a list of spaceship objects to use, the second a list
    of cargo objects to assign.

    The function is used to Solve problem D and is designed for very large
    cargolists and  a list of spaceships that can be used without constraints.

    Maersk will loop through the parcellist and will do the following for each
    cargo object. It calculates the optimal space ship to assign the parcel to
    based on matching the parcels mass to volume ratio and the spaceships
    carrymass to carryvolume ratio. If there is an ship of that class in the
    current fleet with room it will assign the parcel to that ship, otherwise
    it will add another spaceship of this class to the current fleet.

    The algorithm is a greedy constructive algoritm with the mass to volume
    match as it's heuristic.
     '''
    selectedlist = []  # the list that represents the current fleet
    timelist = shiplist
    countrylist = [i.nation for i in shiplist]
    print("You're running the greedy algorithm for problem D. You can now select some options to run it. ")
    bool = input("You can choose to remove the spaceships from a country to improve the solution. Type 'yes' if you want this, any other input will result in a normal run: ")
    bool = bool.lower()
    if bool == 'yes':
        country = input(
            "What country do you want to remove? options: 'Russia', 'Europe', 'USA', 'China' or 'Japan'. (Removing 'USA' gives best solution): ")
        if country in countrylist:
            for i in timelist:
                if i.nation == country:
                    shiplist.remove(i)

    # the list that gets the MV from all spacecship classes
    shipmv = [x.mv for x in shiplist]
    for i in parcellist:
        bool = False
        shipname = calculateoptimal(i, shiplist)
        namelist = [i.name for i in selectedlist]

        if shipname.name not in namelist:
            spacecraft = Spacecraft(shipname.name, shipname.nation,
                                    shipname.payload, shipname.volume,
                                    shipname.mass, shipname.basecost,
                                    shipname.ftw)
            assign(spacecraft, i)
            selectedlist.append(spacecraft)

        elif shipname.name in namelist:
            indexes = []
            for z in range(len(namelist)):
                if namelist[z] == shipname.name:
                    indexes.append(z)

            for y in indexes:
                if checkmove(i, selectedlist[z]):
                    if bool is False:
                        assign(selectedlist[z], i)

                    bool = True
                    break

            if bool is False:
                spacecraft = Spacecraft(shipname.name, shipname.nation,
                                        shipname.payload, shipname.volume,
                                        shipname.mass, shipname.basecost,
                                        shipname.ftw)
                assign(spacecraft, i)
                selectedlist.append(spacecraft)

    sol = solution(selectedlist)
    filename = input("Please name how you want to save this solution: ")
    while filename == "":
        filename = input("Please name how you want to save this solution: ")
    picklename = str(f"results/Newsolutions/{filename}.p")
    pickle.dump(sol, open(picklename, 'wb'))
    print("amount of ships: " + str(len(selectedlist)))
    print("total costs: " + str(calculatetotal(selectedlist)))
    return picklename
