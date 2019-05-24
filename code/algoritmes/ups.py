from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import checkmove
from code.helperfunctions.possiblemoves import possiblemovesA
from code.helperfunctions.assign import assign
from code.helperfunctions.assign import assignfromdict
from code.helperfunctions.assign import clearships
from code.helperfunctions.assign import solution
from collections import Counter
import copy
import pickle
import plotly.graph_objs as go
import plotly.offline as po
import random


def randomsolver(shiplist, parcellist):
    """Takes as input a clear shiplist and parcellist. Randomly assigns parcels
    to spacecrafts. Edits the shiplist and returns the amount of moves of the
    found solution."""
    # do random moves until no more moves possible
    movelist = [1]
    while movelist != []:
        movelist = possiblemovesA(shiplist, parcellist)
        if movelist != []:
            randomchoice = random.randint(0, len(movelist))
            randomchoice -= 1
            move = movelist[randomchoice]
            assign(move[0], move[1])
            parcellist.remove(move[1])
    totalnumber = 0
    for i in shiplist:
        totalnumber += len(i.assigned)
    return totalnumber


def ups(shiplist, cargolist):
    """Takes as input a clear shiplist and parcellist. Randomly assigns parcels
    to spacecrafts n times. Saves the best solution to a pickle file the
    filename of which is returned."""
    # get user input
    n = int(input("How many times do you want to run this algorithm: "))
    while n == "":
        n = int(input("How many times do you want to run this algorithm: "))

    filename = input("Please name how you want to save this solution: ")
    while filename == "":
        filename = input("Please name how you want to save this solution: ")
    picklename = str(f"results/Newsolutions/{filename}") + '.p'

    # keep track of the best solution
    topsolutionnumber = 0
    topsolution = {}
    allsolutions = []
    # run randomsolver n amount times, save the best solution
    for i in range(0, n):
        deeplist = copy.deepcopy(cargolist)
        solution = randomsolver(shiplist, deeplist)
        allsolutions.append(solution)
        if solution > topsolutionnumber:
            topsolutionnumber = solution
            topsolution = shiplist
            pickle.dump(topsolution, open(picklename, 'wb'))
        clearships(shiplist)
    labels, values = zip(*sorted(Counter(allsolutions).items()))
    data = [go.Bar(x=labels, y=values)]
    layout = go.Layout(title=go.layout.Title(
        text=f'Histogram of random generated solutions'),
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Number of parcels in Spacecrafts')),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text='N times the solution of parcels')))
    fig = go.Figure(data=data, layout=layout)
    filenamehisto = input("Please name how you want to save the histogram \
                          visualization: ")
    while filenamehisto == "":
        filenamehisto = input("Please name how you want to save histogram \
                              visualization: ")
    po.plot(fig, filename=f"results/Newvisualizations/{filenamehisto}.html")
    return picklename
