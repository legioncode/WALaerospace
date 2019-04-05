from cargo import *
import numpy as np
import pandas as pd


def main():
    print('hi')



def reader(cargocsv, shipcsv):
    "this function takes in a cargo csv file. and turns it into a dictionary"
    df = pd.read_csv(cargocsv)
    fd = pd.read_csv(shipcsv)
    columnnames = []

    for i in df:
        columnnames.append(i)

    df['mw'] = df[columnnames[1]] / df[columnnames[2]]
    df = df.sort_values(by = ['mw'], ascending = False)
    columnnames.append('mw')
    parceldict = pd.DataFrame.to_dict(df)
    fulldict = {}
    print(df.head())
    for i in columnnames:
        workdict = parceldict[i]

        for x in workdict.keys():
            if x in fulldict.keys():
                currentlist = fulldict[x]
                currentlist.append(workdict[x])
            else:
                fulldict[x] = [workdict[x]]

    return fulldict
    print(fd.head())


reader('CargoList1.csv','SpaceCraft1.csv')
