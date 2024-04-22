import pandas as pd

df = pd.read_csv('dirtydata.csv')

# To Get mean value of Calories column alone , we use in following structure.
# x = df['Calories'].mean()
#
# df.fillna({'Calories':x}, inplace=True)
# print(df.to_string())

# To Get median of Calories column alone , we use following structure.
# y = df['Calories'].median()
#
# df.fillna({'Calories':y},inplace=True)
# print(df.to_string())

# To Get mode of Calories column alone , we use following structure.
# it returns table object(array)
z= df['Calories'].mode()[0]
print(z);

df.fillna({'Calories':z},inplace=True)
print(df.to_string())
