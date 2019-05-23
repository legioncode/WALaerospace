import matplotlib.pyplot as plt
import numpy as np
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
