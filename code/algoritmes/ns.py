from code.helperfunctions.assign import assign
from code.helperfunctions.assign import solution
from code.helperfunctions.assign import calculateoptimal
from code.helperfunctions.assign import calculatetotal
from code.helperfunctions.assign import clearships
from code.helperfunctions.possiblemoves import checkmove
from code.classes.spacecraft import Spacecraft
from collections import Counter
import random
import copy
import pickle
import plotly.graph_objs as go
import plotly.offline as po


def ns(shiplist, parcellist):
    '''ns takes in two arguments, a list of ship objects and a list of
       cargo objects. it assigns parcels to spaceships untill they're full.
       after a spaceship has been filled it chooses a random new ship'''
    randomchoice = random.randint(0, len(shiplist) - 1)
    ship = shiplist[randomchoice]
    spacecraft = Spacecraft(ship.name, ship.nation, ship.payload,
                            ship.volume, ship.mass, ship.basecost,
                            ship.ftw)
    fleet = [spacecraft]

    for i in parcellist:
        if checkmove(i, fleet[-1]):
            assign(fleet[-1], i)
        else:
            randomchoice = random.randint(0, len(shiplist) - 1)
            ship = shiplist[randomchoice]
            spacecraft = Spacecraft(ship.name, ship.nation, ship.payload,
                                    ship.volume, ship.mass, ship.basecost,
                                    ship.ftw)
            fleet.append(spacecraft)
            assign(fleet[-1], i)

    return solution(fleet)


def nsrunner(shiplist, cargolist):
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
        solution = calculatetotal(ns(shiplist, deeplist))
        allsolutions.append(solution)
        if solution < topsolutionnumber:
            topsolutionnumber = solution
            topsolution = shiplist
            pickle.dump(topsolution, open(picklename, 'wb'))
        clearships(shiplist)
    labels, values = zip(*sorted(Counter(allsolutions).items()))
    data = [go.Bar(x=labels, y=values)]
    layout = go.Layout(title=go.layout.Title(
        text=f'Histogram of random generated costs'),
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Cost of solution')),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text='N times the solution of cost')))
    fig = go.Figure(data=data, layout=layout)
    filenamehisto = input("Please name how you want to save the histogram \
                          visualization: ")
    while filenamehisto == "":
        filenamehisto = input("Please name how you want to save histogram \
                              visualization: ")
    po.plot(fig, filename=f"results/Newvisualizations/{filenamehisto}.html")
    return picklename
