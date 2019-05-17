import numpy as np
import pandas as pd
import random
from code.algoritmes.dhl import dhl, dhlonsteroids
from code.helperfunctions.possiblemoves import checkmove, possiblemovecost
from code.helperfunctions.assign import assign, loadstate, clearships

def maersk(shiplist, parcellist):
    print('hoi')
