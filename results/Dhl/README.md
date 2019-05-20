# Results DHL

DHL is a greedy algorithm which takes in three arguments: a list of the available spacecrafts, a list of the parcels to be assigned and the amount of runs. DHL assigns parcels to the ship with the most corresponding mass-volume ratio. Packages that could not be assigned initially are saved in a list and assigned to the most corresponding ship available. The solution which assigns most parcels is saved, which will be in case of draw the least expensive solution. A short summary of the outcomes of DHL with N=5:

> Parcellist 1\
> Packages: 74\
> Costs: $1.460.518.208,77

> Parcellist 2\
> Packages: 76\
> Costs: $1.465.711.566,33

Output files' names end with the number of the used parcellist.
