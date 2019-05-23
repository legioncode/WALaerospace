import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from code.helperfunctions.assign import clearships
from code.algoritmes.ups import randomsolver
from collections import Counter
import plotly.graph_objs as go
import plotly.offline as po
import copy


def visualpackages(shiplist, algorithm):
    filename = input("Please name how you want to save this visualization: ")
    while filename == "":
        filename = input("Please name how you want to save this visualization: ")
    shipbars = [i.name for i in shiplist]
    shipheight = [len(i.assigned) for i in shiplist]
    data = [go.Bar(x=shipbars, y=shipheight)]
    layout = go.Layout(title=f'Number of parcels in ships of {algorithm} algorithm')
    fig = go.Figure(data=data, layout=layout)
    po.plot(fig, filename=f"results/Newvisualizations/{filename}.html")


def massvolumeperc(shiplist, algorithm):
    filename = input("Please name how you want to save this visualization: ")
    while filename == "":
        filename = input("Please name how you want to save this visualization: ")
    shipbars = [i.name for i in shiplist]
    payloadbar = [(i.payload / i.firstpayload * 100) for i in shiplist]
    volumebar = [(i.volume / i.firstvolume * 100) for i in shiplist]
    Payload = go.Bar(x=shipbars, y=payloadbar, name='Payload')
    Volume = go.Bar(x=shipbars, y=volumebar, name='Volume')
    data = [Payload, Volume]
    layout = go.Layout(title=f'Percentage that is left in ships of {algorithm} alogrithm')
    fig = go.Figure(data=data, layout=layout)
    po.plot(fig, filename=f"results/Newvisualizations/{filename}.html")


def progressb(shiplist):
    filename = input("Please name how you want to save this progress visualization: ")
    while filename == "":
        filename = input("Please name how you want to save this progress visualization: ")
    progresslist = []
    totalnumber = 0
    for i in shiplist:
        totalnumber += len(i.assigned)
        progresslist.append(totalnumber)
    progresssteps = [i for i in range(1, len(progresslist))]
    trace = go.Scatter(x=progresssteps, y=progresslist)
    data = [trace]
    layout = go.Layout(title=f'Progress of sending all parcels')
    po.plot(data, filename=f"results/Newvisualizations/{filename}.html")


def nationsparcels(shiplist):
    filename = input("Please name how you want to save this visualization: ")
    while filename == "":
        filename = input("Please name how you want to save this visualization: ")
    nations = [i.nation for i in shiplist]
    parcels = [len(i.assigned) for i in shiplist]
    data = {'Nation': nations, 'Parcels': parcels}
    df = pd.DataFrame(data)
    uniquenat = df.Nation.unique()
    numparcels = [sum(df[df.Nation == i].Parcels) for i in uniquenat]
    data = [go.Bar(x=uniquenat, y=numparcels)]
    layout = go.Layout(title=f'Number of parcels by nation')
    fig = go.Figure(data=data, layout=layout)
    po.plot(fig, filename=f"results/Newvisualizations/{filename}.html")


def shipsbynation(shiplist):  # MOET NOG AAN GEWERKT WORDEN
    shipdict = {}
    for i in shiplist:
        newshipnumber = shipdict[i.nation]
        newshipnumber += 1
        shipdict[i.nation] = newshipnumber
    print(shipdict)


def shipsparcels(shiplist):
    filename = input("Please name how you want to save this visualization: ")
    while filename == "":
        filename = input("Please name how you want to save this visualization: ")
    ships = [i.name for i in shiplist]
    parcels = [len(i.assigned) for i in shiplist]
    data = {'Nation': ships, 'Parcels': parcels}
    df = pd.DataFrame(data)
    uniquenat = df.Nation.unique()
    numparcels = [sum(df[df.Nation == i].Parcels) for i in uniquenat]
    data = [go.Bar(x=uniquenat, y=numparcels)]
    layout = go.Layout(title=f'Number of parcels by ships')
    fig = go.Figure(data=data, layout=layout)
    po.plot(fig, filename=f"results/Newvisualizations/{filename}.html")
