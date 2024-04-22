import pandas as pd

# reads the data from csv file.
df = pd.read_csv('data.csv')

# print the dataframe object that is created by reading 'data.csv'.
print("Normal DataFrame from csv:\n", df, "\n")
print("Type:\n", type(df), "\n")

# print the String object of the dataframe created by reading 'data.csv'.
print("String DataFrame from csv:\n", df.to_string(), "\n")
print("Type:\n", type(df.to_string()), "\n")

# reads the data from json file.
df1 = pd.read_json('opendata.json')

# print the dataframe object that is created by reading 'openData.json'.
print("Normal DataFrame from json:\n", df1, "\n")
print("Type:\n", type(df1), "\n")

# print the String object of the dataframe created by reading 'openData.json'.
print("String DataFrame from json:\n", df1.to_string(), "\n")
print("Type:\n", type(df1.to_string()), "\n")
