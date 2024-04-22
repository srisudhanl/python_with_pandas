import pandas as pd

df = pd.read_csv('dirtydata.csv')

# used to find if the records is duplicated or not.
# it returns true if the row is duplicated, returns false if not.
x = df.duplicated()
print(x)

# used to drop the duplicate row from data frame.
df.drop_duplicates(inplace=True)
print(df)
