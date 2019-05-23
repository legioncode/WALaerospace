# Results Planetexpress

Maersk is a greedy algorithm which takes in two arguments: a list of the available spacecrafts and a list of the parcels to be assigned. Planetexpress takes into account a politicial constraint: the difference in amount of ships between partners must be no larger than one. For each parcel this algorithm calculates which ship would be the best match based on mass-volume ratio. If this ship is full already, another ship of this type will be added to the fleet but only if this does not violate the political constraint. If this does violate the political constraint, the parcel will be assigned to a newly created ship of the partner which had the least ships before. A short summary of the outcomes of Planetexpress:

> Spacecrafts: 50\
> Costs: $ 26.232.541.981,39

