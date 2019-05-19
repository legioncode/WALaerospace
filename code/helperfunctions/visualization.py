import matplotlib.pyplot as plt
import numpy as np
from code.helperfunctions.assign import clearships
from code.algoritmes.ups import randomsolver
from collections import Counter
import copy


def visualpackages(shiplist):
    filename = input("Please name how you want to save this visualization: ")
    while filename == "":
        filename = input("Please name how you want to save this visualization: ")
    shipbars = [i.name for i in shiplist]
    shipheight = [len(i.assigned) for i in shiplist]
    y_pos = np.arange(len(shipbars))
    # Create bars
    plt.bar(y_pos, shipheight)
    plt.xlabel('Ships')
    plt.ylabel('Parcels')
    plt.title('Number of parcels in ships')
    # Create names on the x-axis
    plt.xticks(y_pos, shipbars)

    # Show graphic
    plt.savefig(filename)
    plt.show()



def massvolumeperc(shiplist):
    filename = input("Please name how you want to save this visualization: ")
    while filename == "":
        filename = input("Please name how you want to save this visualization: ")
    shipbars = [i.name for i in shiplist]
    payloadbar = [(i.payload / i.firstpayload * 100) for i in shiplist]
    volumebar = [(i.volume / i.firstvolume * 100) for i in shiplist]
    fig, ax = plt.subplots()
    y_pos = np.arange(len(shipbars))
    width = 0.35
    opacity = 0.8
    rects1 = plt.bar(y_pos, payloadbar, width, alpha=opacity, color='b',
                     label='weight')
    rects2 = plt.bar(y_pos + width, volumebar, width, alpha=opacity, color='g',
                     label='volume')
    plt.xlabel('Ships')
    plt.ylabel('Percentage')
    plt.title('Percentage that is left in ships')
    plt.xticks(y_pos + width, shipbars)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


def randomplot(shiplist, cargolist):
    solutions = []
    for i in range(100):
        deeplist = copy.deepcopy(cargolist)
        solutions.append(randomsolver(shiplist, deeplist))
        clearships(shiplist)
    labels, values = zip(*sorted(Counter(solutions).items()))
    indexes = np.arange(len(labels))
    width = 1

    plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels)
    plt.show()
