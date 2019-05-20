from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
import pandas as pd
import numpy as np


def loadships(shipcsv):
    """Takes in a Spacecraft csv file, and returns a list of spacecraft objects."""
    shipdict = shipreader(shipcsv)
    availableShips = craftassign(shipdict)
    return availableShips


def loadparcels(parcelcsv):
    """Takes in a Cargo csv file, and returns a list of cargo objects."""
    parceldict = cargoreader(parcelcsv)
    availableparcels = parcelassign(parceldict)
    return availableparcels


def cargoreader(cargocsv):
    """Takes in a Cargo csv file, and turns it into a dictionary."""
    df = pd.read_csv(cargocsv)
    columnnames = [i for i in df]
    #print(columnnames)
    df['mv'] = df[columnnames[1]] / df[columnnames[2]]
    cargodict = pd.DataFrame.to_dict(df, orient='index')
    return cargodict


def shipreader(csv):
    """Takes in a Spacecraft csv file, and turns it into a dictionary."""
    df = pd.read_csv(csv)
    transportdict = pd.DataFrame.to_dict(df, orient='index')
    return transportdict


def craftassign(shipdict):
    """Takes in a Spacecraft dictionary, and returns a shiplist."""
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
                basecostname = name
            elif value == 'ftw':
                ftwname = name
            else:
                break
        spacecraft = Spacecraft(spacecraftname, nationname, payloadname,
                                volumename, massname, basecostname, ftwname)
        shiplist.append(spacecraft)
    return shiplist


def parcelassign(parceldict):
    """Takes in a Cargo dictionary, and returns a cargolist."""
    cargolist = []
    for key, cargo in parceldict.items():
        for value, name in cargo.items():
            if value == 'parcel_ID':
                id_name = name
            elif value == 'mass (kg)':
                massname = name
            elif value == 'volume (m^3)':
                sizename = name
            elif value == 'mv':
                mvname = name
            else:
                break
        parcellist = Cargo(id_name, massname, sizename, mvname)
        cargolist.append(parcellist)
    return cargolist
