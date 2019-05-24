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
    layout = go.Layout(title=go.layout.Title(
        text=f'Number of parcels in ships of {algorithm} algorithm'),
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Ships')),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text='Number of parcels')))
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
    layout = go.Layout(title=go.layout.Title(
        text=f'Percentage that is left in ships of {algorithm} alogrithm'),
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Ships')),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text='Percentage')))
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
    layout = go.Layout(title=go.layout.Title(
        text=f'Progress of sending all parcels'),
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Ships sent')),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text='Parcels sent')))
    fig = go.Figure(data=data, layout=layout)
    po.plot(fig, filename=f"results/Newvisualizations/{filename}.html")


def progresstwo(shiplist1, algoname, shiplist2, algoname2):
    filename = input("Please name how you want to save this progress visualization: ")
    while filename == "":
        filename = input("Please name how you want to save this progress visualization: ")
    progresslist1 = []
    progresslist2 = []
    totalnumber1 = 0
    totalnumber2 = 0
    for i in shiplist1:
        totalnumber1 += len(i.assigned)
        progresslist1.append(totalnumber1)
    for i in shiplist2:
        totalnumber2 += len(i.assigned)
        progresslist2.append(totalnumber2)
    progresssteps1 = [i for i in range(1, len(progresslist1))]
    progresssteps2 = [i for i in range(1, len(progresslist2))]
    trace1 = go.Scatter(x=progresssteps1, y=progresslist1, name=algoname)
    trace2 = go.Scatter(x=progresssteps2, y=progresslist2, name=algoname2)
    data = [trace1, trace2]
    layout = go.Layout(title=go.layout.Title(
        text=f'Progress of sending all parcels'),
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Ships sent')),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text='Parcels sent')))
    fig = go.Figure(data=data, layout=layout)
    po.plot(fig, filename=f"results/Newvisualizations/{filename}.html")


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
    layout = go.Layout(title=go.layout.Title(
        text=f'Number of parcels by nation'),
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Nations')),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text='Parcels sent')))
    fig = go.Figure(data=data, layout=layout)
    po.plot(fig, filename=f"results/Newvisualizations/{filename}.html")


'''def shipsbynation(shiplist):  # MOET NOG AAN GEWERKT WORDEN
    shipdict = {}
    for i in shiplist:
        newshipnumber = shipdict[i.nation]
        newshipnumber += 1
        shipdict[i.nation] = newshipnumber
    print(shipdict)
'''


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
    layout = go.Layout(title=go.layout.Title(
        text=f'Number of parcels by ships'),
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Ships')),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text='Parcels sent')))
    fig = go.Figure(data=data, layout=layout)
    po.plot(fig, filename=f"results/Newvisualizations/{filename}.html")
