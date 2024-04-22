import pandas as pd

df = pd.read_csv('dirtydata.csv')

# to format the date to date format , we use to_datetime().
# 'errors = "coerce"' => used to convert any elements that cannot be parsed into NaT (Not a Time) values instead of raising an error.
df["Date"] = pd.to_datetime(df["Date"], format='mixed', errors='coerce')
print(df)

df.dropna(subset=["Date"], inplace=True)
print(df)

# To iterate the docs.
for x in df.index:
    if df.loc[x,"Duration"] > 120:
        df.loc[x,"Duration"] = 120
print(df)