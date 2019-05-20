# Results DHL

Hillclimber is an iterative algorithm which takes as beginstate a solution from the dhl-algorithm. From this solution, the hillclimer
randomly takes two packages from two different ships, checks whether they can be switched, and does so if this improves the current solution.
For the belowmentioned results, the hillclimber algorithm performed 10.000.000 iterations.

> Parcellist 1\
> Beginstate\
> Packages: 68\
> Costs: $1.459.823.258,12\
> After Hillclimber\
> Packages: 96\
> Costs: $1.468.735.066

> Parcellist 2\
> Beginstate\
> Packages: 71\
> Costs: $1.464.746.287,58\
> After Hillclimber\
> Packages: 84\
> Costs: $1.469.398.664,37

Output files' names end with the number of the used parcellist.
