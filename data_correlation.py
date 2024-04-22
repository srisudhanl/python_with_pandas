import pandas as pd
import numpy as np

df = pd.read_csv('dirtydata.csv')
df["Date"] = pd.to_datetime(df["Date"], format='mixed', errors='coerce')


# is used to find the correlation between the data
print("Old data correlation:\n",df.corr(),"\n")

df1 = pd.read_csv('cleaned_data.csv')
df1["Date"] = pd.to_datetime(df1["Date"])

print("Cleaned Data Correlation:\n",df1.corr(),"\n")