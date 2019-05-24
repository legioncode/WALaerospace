from code.algoritmes.hillclimber import hillclimber
from code.helperfunctions.visualization import massvolumeperc
from code.helperfunctions.visualization import visualpackages
import pickle


def getProblem():
    """This function prompts the user for which problem they want to solve and
    returns this problem"""
    problem = input("Welcome to space freight! Do you want to optimize a: \
                    amount of parcels, or b: costs. Choose 'a' or \
                    'b' ").lower()
    while problem not in ('a', 'b'):
        problem = input("Please choose 'a' or 'b': ").lower()
    return problem


def getParcellist():
    """This function prompts the user for which parcellist they want to use
    and returns this list"""
    parcels = int(input("Which list of packages do you want to use? Choose '1'\
                  or '2': "))
    while parcels not in (1, 2, 3):
        parcels = int(input("Please choose '1' or '2': "))
    if parcels == 1:
        return 'data/CargoList1.csv'
    else:
        return 'data/CargoList2.csv'


def getAlgorithmA():
    """This function prompts the user for which algorithm they want to use
    and returns this"""
    algorithm = input("What type of algorithm do you want to use? Choose \
                    'random', 'greedy' or 'beamsearch': ").lower()
    while algorithm not in ('random', 'greedy', 'beamsearch'):
        algorithm = input("Please choose 'random', 'greedy' or \
                          'beamsearch': ").lower()
    if algorithm == 'greedy':
        algorithm = input(
            "Good choice! We have multiple greedy algorithms ready for you. \
            Please choose 'postnl', 'dhl' or 'flessenpost': ").lower()
        while algorithm not in ('postnl', 'dhl', 'flessenpost'):
            algorithm = input("Please choose 'postnl', 'dhl' or 'flessenpost': ").lower()
    return algorithm


def getHillclimber(shiplist, parcellist):
    """This function prompts the user to choose whether they want to use a \
    hillclimber or not and returns the results if so"""
    choice = input(
        "Do you want to try to bring more packages by running a hillclimber on \
        this solution? Choose 'yes' or 'no': ").lower()
    while choice not in ('yes', 'no'):
        choice = input("Please choose 'yes' or 'no': ").lower()
    if choice == 'yes':
        solution = hillclimber(shiplist, parcellist)
        packedships = pickle.load(open(solution, "rb"))
        visualpackages(packedships, 'hillclimber')
        massvolumeperc(packedships, 'hillclimber')


def getConstraint():
    """This function prompts the user for an additional constraint and returns
    the name of the appropriate algorithm"""
    constraint = input(
        "Do you want to make sure Trump's spacecrafts don't launch more often \
        than Poetin's? Choose 'yes' or 'no': ").lower()
    while constraint not in ('yes', 'no'):
        constraint = input(
            "Do you want to make sure Trump's spacecrafts don't launch more \
            often than Poetin's? Choose 'yes' or 'no': ").lower()
    return constraint
