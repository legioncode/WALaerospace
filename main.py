from code.algoritmes.beam import Beam
from code.algoritmes.dhl import dhl
from code.algoritmes.dhl import dhlonsteroids
from code.algoritmes.flessenpost import flessenpost
from code.algoritmes.hillclimber import hillclimber
from code.algoritmes.maersk import maersk
from code.algoritmes.planetexpress import planetexpress
from code.algoritmes.postnl import postnl
from code.algoritmes.ups import randomsolver
from code.algoritmes.ups import ups
from code.helperfunctions.assign import calculatepackages
from code.helperfunctions.assign import calculatetotal
from code.helperfunctions.mainhelper import getAlgorithmA
from code.helperfunctions.mainhelper import getConstraint
from code.helperfunctions.mainhelper import getHillclimber
from code.helperfunctions.mainhelper import getParcellist
from code.helperfunctions.mainhelper import getProblem
from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.helperfunctions.visualization import massvolumeperc
from code.helperfunctions.visualization import progressb
from code.helperfunctions.visualization import visualpackages
import pickle


def main():
    problem = getProblem()
    if problem == 'a':
        shiplist = loadships('data/SpaceCraft1.csv')
        parcels = getParcellist()
        parcellist = loadparcels(parcels)
        algorithm = getAlgorithmA()
        if algorithm == 'random':
            solution = ups(shiplist, parcellist)
        elif algorithm == 'postnl':
            solution = postnl(shiplist, parcellist)
        elif algorithm == 'dhl':
            solution = dhlonsteroids(shiplist, parcellist)
        elif algorithm == 'flessenpost':
            solution = flessenpost(shiplist, parcellist)
        elif algorithm == 'beamsearch':
            solution = Beam(shiplist, parcellist)
        packedships = pickle.load(open(solution, "rb"))
        visualpackages(packedships, algorithm)
        massvolumeperc(packedships, algorithm)
        if algorithm == 'dhl':
            getHillclimber(packedships, parcellist)
        amount = calculatepackages(packedships)
        for ship in packedships:
            ship.calculate()
        cost = calculatetotal(packedships)
        print(f"Ready for takeoff! You are bringing {amount} packages to a cost of ${cost}")

    else:
        shiplist = loadships('data/SpaceCraft2.csv')
        parcellist = loadparcels('data/CargoList3.csv')
        constraint = getConstraint()
        if constraint == 'no':
            solution = maersk(shiplist, parcellist)
        else:
            solution = planetexpress(shiplist, parcellist)


if __name__ == "__main__":
    main()
