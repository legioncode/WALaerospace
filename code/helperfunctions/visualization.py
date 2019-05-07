import matplotlib.pyplot as plt
import numpy as np


def visual(shiplist):
    shipbars = [i.name for i in shiplist]
    shipheight = [len(i.assigned) for i in shiplist]
    y_pos = np.arange(len(shipbars))
    # Create bars
    plt.bar(y_pos, shipheight)

    # Create names on the x-axis
    plt.xticks(y_pos, shipbars)

    # Show graphic
    plt.show()
