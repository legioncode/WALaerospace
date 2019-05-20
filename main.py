from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.algoritmes.dhl import dhl, dhlonsteroids
from code.algoritmes.ups import ups, randomsolver
from code.algoritmes.postnl import postnl
from code.helperfunctions.visualization import visualpackages, massvolumeperc, randomplot
from code.algoritmes.flessenpost import flessenpost
import math
from code.algoritmes.beam import Beam
from code.algoritmes.maersk import *
import pickle
from collections import Counter
from code.algoritmes.hillclimber import hillclimber
from code.helperfunctions.assign import calculatetotal, calculatepackages

def getProblem():
    problem = input("Welcome to space freight! Choose problem 'a' or 'b': ")
    while problem not in ('a', 'b'):
        problem = input("Please choose 'a' or 'b': ")
    return problem

def getParcellist():
    parcels = int(input("Which list of packages do you want to use? Choose '1' or '2': "))
    while parcels not in (1, 2, 3):
        parcels = int(input("Please choose '1' or '2': "))
    if parcels == 1:
        return 'data/CargoList1.csv'
    else:
        return 'data/CargoList2.csv'

def getAlgorithm():
    algorithm = input("What type of algorithm do you want to use? Choose 'random', 'greedy' or 'beamsearch': ")
    while algorithm not in ('random', 'greedy', 'beamsearch'):
        algorithm = input("Please choose 'random', 'greedy' or 'beamsearch': ")
    if algorithm == 'greedy':
        algorithm = input("Good choice! We have multiple greedy algorithms ready for you. Please choose 'postnl', 'dhl' or 'flessenpost': ")
        while algorithm not in ('postnl', 'dhl', 'flessenpost', 'd'):
            algorithm = input("Please choose 'postnl', 'dhl' or 'flessenpost': ")
    return algorithm

def getHillclimber(shiplist, parcellist):
    choice = input("Do you want to try to bring more packages by running a hillclimber on this solution? Choose 'yes' or 'no': ")
    while choice not in ('yes', 'no'):
        choice = input("Please choose 'yes' or 'no': ")
    if choice == 'yes':
        solution = hillclimber(shiplist, parcellist)
        packedships = pickle.load(open(solution, "rb"))
        visualpackages(packedships)
        massvolumeperc(packedships)
        amount = calculatepackages(packedships)
        for ship in packedships:
            ship.calculate()
        cost = calculatetotal(packedships)
        print(f"Ready for takeoff! You are bringing {amount} packages to a cost of ${cost}")

def main():
    usedgreedy = None
    problem = getProblem()
    if problem == 'a':
        shiplist = loadships('data/SpaceCraft1.csv')
        parcels = getParcellist()
        parcellist = loadparcels(parcels)
        algorithm = getAlgorithm()

        if algorithm == 'random':
            solution = ups(shiplist, parcellist)
            packedships = pickle.load(open(solution, "rb"))
            visualpackages(packedships)
            massvolumeperc(packedships)

        elif algorithm == 'postnl':
            solution = postnl(shiplist, parcellist)
            packedships = pickle.load(open(solution, "rb"))
            visualpackages(packedships)
            massvolumeperc(packedships)

        elif algorithm == 'dhl':
            solution = dhlonsteroids(shiplist, parcellist)
            packedships = pickle.load(open(solution, "rb"))
            visualpackages(packedships)
            massvolumeperc(packedships)
            getHillclimber(packedships, parcellist)

        elif algorithm == 'flessenpost':
            solution = flessenpost(shiplist, parcellist)
            packedships = pickle.load(open(solution, "rb"))
            visualpackages(packedships)
            massvolumeperc(packedships)

        elif algorithm == 'beamsearch':
            solution = Beam(shiplist, parcellist)
            packedships = pickle.load(open(solution, "rb"))
            visualpackages(packedships)
            massvolumeperc(packedships)

        amount = calculatepackages(packedships)
        for ship in packedships:
            ship.calculate()
        cost = calculatetotal(packedships)
        print(f"Ready for takeoff! You are bringing {amount} packages to a cost of ${cost}")

    else:
        shiplist = loadships('data/SpaceCraft2.csv')
        parcellist = loadparcels('data/CargoList3.csv')
        maersk(shiplist, parcellist, False)

if __name__ == "__main__":
    main()
