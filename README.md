# WALaerospace :rocket:

## The Problem
In Space Freight we want to find the optimal assignment of parcels to spacecrafts for transport to the International Space Station (ISS). The first problem is about assigning parcels from the first cargolist to four spacecrafts. More specifically, we want to find out whether it is possible to transport from this list 97 parcels. In the second problem, we want to find the maximum set of parcels that can be transported, where in case of multiple outcomes we go for the least expensive solution. This will be repeated for the third problem, now using the second cargolist. Now we get access to two more spacecrafts. For the fourth problem we compose a fleet of spacecrafts to transport the parcels of cargolist #3, whereby spacecrafts can do multiple flights and we look for the least expensive solution again. Lastly, in problem 5 we take into consideration a political constraint whereby spacecrafts from different countries must be used a comparable amount of times. Specifically, the difference in amount of flights between countries' spacecrafts can be no greater than 1. We aim for a solution where a maximum, if not thé maximum, amount of packages can be transported. If there are multiple assignment solutions, we go for the least expensive option.

## Upper- and Lowerbound(s)
**For problem a,b,c**\
The costs for transport using four fully loaded spaceships are $1.469.436.478 (upperbound).

> Cygnus: (((7400 + 2000) x 0,73 / (1 - 0,73)) x 1000) + 390.000.000 = $ 415.387.778\
> Progress: (((7020 + 2400) x 0,74 / (1 - 0,74)) x 1000) + 175.000.000 = $ 201.810.769\
> Kounotori: (((10500 + 5200) x 0,71 / (1 - 0,71)) x 1000) + 420.000.000 = $ 458.437.931\
> Dragon: (((12200 + 6000) x 0,72 / (1 - 0,72)) x 1000) + 347.000.000 = $ 393.800.000

Transporting the lightest cargo from cargolist 1 (CL1#38) with the least expensive spacecraft (Progress) costs $195.267.176,923 (lowerbound).

> (((7020 + 100,9) x 0,74 / (1 - 0,74)) x 1000) + 175.000.000 = $195.267.176,923

Transporting the lightest cargo from cargolist 2 (CL2#67) with the least expensive spacecraft (Progress) costs $195 303 607,692 (lowerbound).

> (((7020 + 113,7) x 0,74 / (1 - 0,74)) x 1000) + 175.000.000 = $195 303 607,692
