import pandas as pd

# prints the directories in pandas.
print(dir(pd), "\n");

# data as dictionary
data = {
    "Languages": ['Flutter', 'Dart', 'Typescript', 'Python'],
    "profeciency": [4, 3.5, 3.5, 3.3],
}

x = pd.DataFrame(data);
# print the dictionary data as dataframe
print(x, "\n");
# print the type of variable that constist of dataFrame object.
print(type(x), "\n");
# print the version of pandas.
print(pd.__version__);
