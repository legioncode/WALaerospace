# Space Freight by WAL :rocket:

In Space Freight we find solutions for assignment of parcels to spacecrafts for transport to the International Space Station (ISS). This is a typical Constraint Optimization Problem (COP): there are multiple possible solutions, which are not necessarily all as good, and which have to meet certain requirements i.e. constraints. Depending on the constraints, solutions can be optimized based on the following outcomes:

> 1: The amount of packages that can be transported
> 2: The costs of the transport

## Upper- and Lowerbound(s)
**For problem a,b,c**\
The costs for transport using four fully loaded spaceships are $1.469.436.478 (upperbound).

> Cygnus: (((7400 + 2000) x 0,73 / (1 - 0,73)) x 1000) + 390.000.000 = $ 415.414.815\
> Progress: (((7020 + 2400) x 0,74 / (1 - 0,74)) x 1000) + 175.000.000 = $ 201.810.770\
> Kounotori: (((10500 + 5200) x 0,71 / (1 - 0,71)) x 1000) + 420.000.000 = $ 458.437.932\
> Dragon: (((12200 + 6000) x 0,72 / (1 - 0,72)) x 1000) + 347.000.000 = $ 393.800.000

Transporting the lightest cargo from cargolist 1 (CL1#38) with the least expensive spacecraft (Progress) costs $195.267.176,923 (lowerbound).

> (((7020 + 100,9) x 0,74 / (1 - 0,74)) x 1000) + 175.000.000 = $195.267.176,923

Transporting the lightest cargo from cargolist 2 (CL2#67) with the least expensive spacecraft (Progress) costs $195 303 607,692 (lowerbound).

> (((7020 + 113,7) x 0,74 / (1 - 0,74)) x 1000) + 175.000.000 = $195.303.607,692

For the second part of the project (problem d and e) there are two more spacecrafts added.
> TianZhou: (((13500 + 6500) x 0,75 / (1 - 0,75)) x 1000) + 412.000.000 = $ 472.000.000\
> Verne ATV: (((20500 + 7500) x 0,72 / (1 - 0,72)) x 1000) + 1.080.000.000 = $ 1.152.000.000
