from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships
from code.algoritmes.dhl import dhl, dhlonsteroids
from code.algoritmes.ups import ups, randomsolver
from code.algoritmes.postnl import postnl
#from code.helperfunctions.visualization import visualpackages, massvolumeperc, randomplot
from code.algoritmes.flessenpost import flessenpost
#from code.helperfunctions.visualization import visualpackages, massvolumeperc
import math
from code.helperfunctions.cargototals import totals
from code.algoritmes.beam import Beam
from code.algoritmes.maersk import *
import pickle
from collections import Counter
from code.algoritmes.hillclimber import hillclimber

def getProblem():
    problem = input("Welcome to space freight! Choose problem 'a' or 'b': ")
    while problem not in ('a', 'b'):
        problem = input("Please choose 'a' or 'b': ")
    return problem

def getParcellist():
    parcels = int(input("Which list of packages do you want to use? Choose '1' or '2': "))
    while parcels not in (1, 2):
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
        algorithm = input("Good choice! We have multiple greedy algorithms ready for you. Please choose 'postnl', 'dhl', 'dhlonsteroids' or 'flessenpost': ")
        while algorithm not in ('postnl', 'dhl', 'flessenpost'):
            algorithm = input("Please choose 'postnl', 'dhl' or 'flessenpost': ")
    return algorithm

def getHillclimber():
    hillclimber = input("Do you want to try to bring more packages by running a hillclimber on this solution? Choose 'yes' or 'no': ")
    while hillclimber not in ('yes', 'no'):
        hillclimber = input("Please choose 'yes' or 'no': ")
    return hillclimber

def main():
    problem = getProblem()
    if problem == 'a':
        shiplist = loadships('data/SpaceCraft1.csv')
        parcels = getParcellist()
        parcellist = loadparcels(parcels)
        algorithm = getAlgorithm()
        if algorithm == 'random':
            solution = randomsolver(shiplist, parcellist)
        elif algorithm == 'postnl':
            solution = postnl(shiplist, parcellist)
        elif algorithm == 'dhl':
            solution = dhl(shiplist, parcellist)
        elif algorithm == 'dhlonsteroids':
            solution = dhlonsteroids(shiplist, parcellist)
        elif algorithm == 'flessenpost':
            solution = flessenpost(shiplist, parcellist)
        elif algorithm == 'beamsearch':
            solution = Beam(shiplist, parcellist)
        print("Ready for takeoff!")
        total = 0
        for ship in solution:
            print(f"Spacecraft {ship.name} carries {len(ship.assigned)} packages")
            for parcel in ship.assigned:
                total += 1
        print(f"In total you can bring {total} packages")

        hillclimber = getHillclimber()
        if hillclimber == 'yes':
            hillclimber(solution, parcellist)

    else:
        print('under construction')

if __name__ == "__main__":
    main()
