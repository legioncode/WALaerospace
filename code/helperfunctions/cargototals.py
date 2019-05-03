from code.helperfunctions.readers import loadparcels
from code.helperfunctions.readers import loadships

def totals(parcellist, shiplist):
    tpw = 0
    tpv = 0
    for parcel in parcellist:
        tpw += parcel.mass
        tpv += parcel.size

    tsw = 0
    tsv = 0
    for ship in shiplist:
        tsw += ship.payload
        tsv += ship.volume

    print(f"total weight parcels = {tpw}")
    print(f"total volume parcels = {tpv}")
    print(f"total weight ships can carry = {tsw}")
    print(f"total volume ships can carry = {tsv}")

#main('data/CargoList1.csv', 'data/SpaceCraft1.csv')
