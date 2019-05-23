def sortParcels(parcellist):
    """Takes in a parcellist. Sorts the parcels in ascending order based on
    their mass-volume ratios.
    Returns a sorted parcellist."""
    sorted_parcels = sorted(parcellist, key=lambda cargo: cargo.mv,
                            reverse=False)
    return sorted_parcels


def sortSpacecrafts(shiplist):
    """Takes in a shiplist. Sorts the spacecrafts in ascending order based on
    their payload mass-volume ratios.
    Returns a sorted shiplist."""
    sorted_ships = sorted(shiplist, key=lambda spacecraft: spacecraft.mv,
                          reverse=False)
    return sorted_ships
