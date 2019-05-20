# Results PostNL

PostNL is a greedy algorithm which takes in two arguments: a list of the available spacecrafts and a list of the parcels to be assigned. PostNL sorts both lists based on the mass-volume ratios of the objects they contain, and starts assigning packages from the middle of both lists towards the left- and right ends. Packages that could not be assigned initially are saved in a list and randomly assigned to the initial solution if possible. A short summary of the outcomes of PostNL:

> Parcellist 1\
> Packages: 86\
> Costs: $ 1.467.338.973,03

> Parcellist 2\
> Packages: 78\
> Costs: $ 1.469.273.842,28

Output files' names end with the number of the used parcellist.
