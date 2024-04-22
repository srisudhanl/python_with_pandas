import pandas as pd

df = pd.read_csv("dirtydata.csv")
df["Date"] = pd.to_datetime(df["Date"], format='mixed', errors='coerce')
df.dropna(subset=["Date"], inplace=True)
df.drop_duplicates(inplace=True)
df.fillna({'Duration': 60, 'Pulse': 110, 'Maxpulse': 130, 'Calories': 350.5}, inplace=True)

# To save dataframe to csv we use to_csv().
df.to_csv('cleaned_data.csv')

# To save dataframe to json we use to_json().
df.to_json('cleaned_data.json')
