from cargo import *
import numpy as np
import pandas as pd


def main():
    print('hi')



def cargoreader(csv):
    "this function takes in a cargo csv file. and turns it into a"
    df = pd.read_csv(csv)
    print(df.head())
    columnnames = []
    for i in df:
        columnnames.append(i)
    parceldict = pd.DataFrame.to_dict(df)
    fulldict = {}
    for i in columnnames:
        workdict = parceldict[i]
        for x in workdict.keys():
            if x in fulldict.keys():
                currentlist = fulldict[x]
                currentlist.append(workdict[x])
            else:
                fulldict[x] = [workdict[x]]
    print(fulldict)
cargoreader('CargoList1.csv')
