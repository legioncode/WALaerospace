# Space Freight by WAL :rocket:

In Space Freight we find solutions for assignment of parcels to spacecrafts for transport to the International Space Station (ISS). Multiple lists of parcels and ships are available. This is a typical Constraint Optimization Problem (COP): there are multiple possible solutions, which are not necessarily all as good, and which have to meet certain requirements i.e. constraints. Depending on the constraints, solutions can be optimized based on the following outcomes:

> 1: The amount of packages that can be transported\
> 2: The costs of the transport

The best assignment we found when optimizing the amount of packages that can be transported, was the result of running a hillclimber algorithm on the result of a greedy algorithm:

> Parcellist 1\
> Packages: 96\
> Costs: $1.468.735.066

> Parcellist 2\
> Packages: 84\
> Costs: $1.469.398.664,37

## Getting Started
### Prerequisites

All code for this project is written in Python 3.7 All required packages to run this code can be found in requirements.txt and easily installed by running the following command:

```python
pip install -r requirements.txt
```
### Structure
All data we have available for this case can be found under **data**. Pythonscripts are divided into the categories **classes**, **helperfunctions** and **algorithms** all of which are accomodated in the **code** folder. Output of all different algorithms is available in the **output** folder.

### Testing
If you want to run (part of) the code yourself, download the code from this repository, in your terminal navigate to the relevant directory and run the following command:

```python
python main.py
```
On the command line you can then indicate which optimization of the problem you want to focus on. If applicable, you will be asked to choose one of the available parcellists for your problem after which you get to choose which of the algorithms you want to run. Some algorithms require some additional input, in case for which you will be prompted. Last but not least, you get to define how you want to save your newly generated output and get the results both textually as visually.

## Authors
• Axel Huting\
• Wytze Dijkstra\
• Lotte Heek

## Acknowledgements
• the course 'heuristieken' from UVA
