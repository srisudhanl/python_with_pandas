import pandas as pd
import matplotlib.pyplot as mp

df = pd.read_csv('dirtydata.csv')
df1 = pd.read_csv('cleaned_data.csv')

# used to create the plot using the data present in the dataframes
df.plot()
df1.plot()

# used to display the plots that were generated.
mp.show()