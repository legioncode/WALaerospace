import pandas as pd
import numpy as np

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


cargoreader('CargoList1.csv')
