def sortParcels(parcellist):
    """Sorts the parcels in ascending order based on their mass-volume ratios"""
    sorted_parcels = sorted(parcellist, key=lambda cargo: cargo.mv, reverse=False)
    return sorted_parcels


def sortSpacecrafts(shiplist):
    """Sorts the spacecrafts in ascending order based on their payload mass-volume ratios"""
    sorted_ships = sorted(shiplist, key=lambda spacecraft: spacecraft.mv, reverse=False)
    return sorted_ships
