import pandas as pd

df = pd.read_csv('dirtydata.csv')
df1 = pd.read_csv('dirtydata.csv')
df2 = pd.read_csv('dirtydata.csv')
df3 = pd.read_csv('dirtydata.csv')

# if we need to delete the row which doesn't contain data in any of its column is deleted using 'dropna()'.
# it doesn't modify original data frame.
x = df.dropna()
print("Using dropna() without inplace:\n", x.to_string(), "\n")

# if we need to delete the row which doesn't contain data in any of its column is deleted using 'dropna(inplace=true)'.
# it changes the main dataframe itself.
df1.dropna(inplace=True)
print("Using dropna() with inplace:\n", df1.to_string(), "\n")

# if we need to replace the data where it is not present in any one of the column , we can use 'fillna("<replace_term>")'.
# it doesn't modify original data frame.
y = df2.fillna('null')
print("Using fillna() without inplace:\n",y.to_string(),"\n")

# if we need to replace the data where it is not present in any one of the column , we can use 'fillna("<replace_term>",inplace=true)'.
# it modifies original data frame.
df3.fillna('null',inplace=True)
print("Using fillna() without inplace:\n",df3.to_string(),"\n")

# if we need to fill different values for each column where null value present can be achieved in following manner.
z = df2.fillna({'Duration': 60,'Date':'2020/12/22','Pulse': 110,'Maxpulse': 130,'Calories':350.5})
print(z.to_string())