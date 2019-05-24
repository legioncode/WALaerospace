# Results

This folder contains the results per algorithm. For each algorithm there is a pickle document containing the solution in the form of a shiplist: a list of the used spacecrafts and their attributes. Furthermore several html formatted visualisations are available, which can be opened only after download because of github constraints regarding documents' size. To open the pickle file use the following code, where filename is the name of the pickle file you want to open:

```python
solution = pickle.load(open(filename, "rb"))
```
