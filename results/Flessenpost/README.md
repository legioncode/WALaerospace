# Results Flessenpost

This folder contains the results of Flessenpost. Flessenpost is a greedy algorithm which takes in two arguments: a list of the available spacecrafts and a list of the parcels to be assigned. Flessenpost sorts both lists based on the mass-volume ratios of the objects they contain, and starts assigning parcels to spacecrafts beginning with the largest ratios, initially skipping the outliers of the parcellist. Packages that could not be assigned initially are saved in a list and randomly assigned to the initial solution if possible, after which the outliers are taken into consideration as well. A short summary of the outcomes of Flessenpost:

> Parcellist 1\
> Packages: 89\
> Costs: $ 1.429.065.732,53

> Parcellist 2\
> Packages: 76\
> Costs: $ 1.429.065.732,53

Output files' names end with the number of the used parcellist.
