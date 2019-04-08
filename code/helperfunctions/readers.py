import pandas as pd
import numpy as np
from spacecraft import *
from cargo import *

def loadships(shipcsv):
    shipdict = shipreader(shipcsv)
    availableShips = craftassign(shipdict)
    return availableShips

def loadparcels(parcelcsv):
    parceldict = cargoreader(parcelcsv)
    availableparcels = parcelassign(parceldict)
    return availableparcels

def cargoreader(cargocsv):
    "this function takes in a cargo csv file. and turns it into a dictionary"
    df = pd.read_csv(cargocsv)
    columnnames = [i for i in df]

    df['mw'] = df[columnnames[1]] / df[columnnames[2]]
    df = df.sort_values(by = ['mw'], ascending = False)
    cargodict = pd.DataFrame.to_dict(df, orient = 'index')
    return cargodict


def shipreader(csv):
    df = pd.read_csv(csv)
    transportdict = pd.DataFrame.to_dict(df, orient = 'index')
    return transportdict

def craftassign(shipdict):
    shiplist = []
    for key, craft in shipdict.items():
        for value, name in craft.items():
            if value == 'spacecraft':
                spacecraftname = name
            elif value == 'nation':
                nationname = name
            elif value == 'payload':
                payloadname = name
            elif value == 'volume':
                volumename = name
            elif value == 'mass':
                massname = name
            elif value == 'cost':
                costname = name
            elif value == 'ftw':
                ftwname = name
            else:
                break
        spacecraft = Spacecraft(spacecraftname,nationname,payloadname,volumename,massname,costname,ftwname)
        shiplist.append(spacecraft)
    return shiplist

def parcelassign(parceldict):
    cargolist = []
    for key, cargo in parceldict.items():
        for value, name in cargo.items():
            if value == 'parcel_ID':
                id_name = name
            elif value == 'mass (kg)':
                massname = name
            elif value == 'volume (m^3)':
                sizename = name
            elif value == 'mw':
                mwname = name
            else:
                break
        parcellist = Cargo(id_name,massname,sizename,mwname)
        cargolist.append(parcellist)
    return cargolist
