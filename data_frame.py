import pandas as pd

# data as dictionary
data = {
    "Languages": ['Flutter', 'Dart', 'Typescript', 'Python'],
    "profeciency": [4, 3.5, 3.5, 3.3],
}

df = pd.DataFrame(data)

# prints the dictionary data as dataFrame.
print("Normal DataFrame:\n", df, "\n")

# To print certain data from the dataFrame use '.loc[<index_value>]'.
print("Print certain data from dataframe using loc[<index_value>]:\n", df.loc[0], "\n")

# To print more than one data from the dataframe using 'loc[<list_of_index_values>]'.
print("Print more than one data from dataframe using 'loc[<list_of_index_values>]:\n", df.loc[[0, 1]], "\n")
print("Print more than one data from dataframe using 'loc[<list_of_index_values>]:\n", df.loc[[0, 1, 3]], "\n")

# Custom indexing of the data using dataFrame.
df1 = pd.DataFrame(data, index=["Lang1", "Lang2", "Lang3", "Lang4"])
print("Custom indexed DataFrame:\n", df1, "\n")

# To print certain data from the dataFrame using custom index.
print("Print certain data from dataframe using custom index:\n", df1.loc["Lang2"], "\n")

# To print more than one data from the dataframe using custom index.
print("Print more than one data from dataframe using custom index:\n", df1.loc[["Lang1", "Lang3"]], "\n")
