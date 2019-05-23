# Results

This folder contains the results per algorithm. For each algorithm there is a pickle document containing the solution in the form of a shiplist: a list of the used spacecrafts and their attributes. Furthermore two html formatted visualisations are available, displaying the distribution of packages and the mass and volume each ship has left. To open the pickle file use the following code, where filename is the name of the pickle file you want to open:

```python
solution = pickle.load(open(filename, "rb"))
```
