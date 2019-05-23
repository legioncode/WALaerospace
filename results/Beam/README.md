# Results Beam

Beam is a combination of greedy algorithm and a breadth first algorithm, which takes in three arguments: a list of the available spacecrafts, a list of the parcels to be assigned and the preferred beamwidht. Beam starts of by creating an empty packinglist object, and computing its children. Only the chosen n amount best children are then explored further. Children are ranked based on how well their last move's package's mass-volume ratio matches with the mass-volume ratio of the ship it is assigned to. A short summary of the outcomes of Beam:

> Parcellist 1\
> Packages: 90\
> Costs: $ 1.466.318.846,65

> Parcellist 2\
> Packages: 76\
> Costs: $ 1.466.538.279,32

Output files' names end with the number of the used parcellist.


