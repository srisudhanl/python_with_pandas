import pandas as pd

df = pd.read_csv('data.csv')

# if file present in some other location.
# df = pd.read_csv('<full_file_path_of_file>')

# if the data in csv file is seperated by character other than ',' , "sep=" is used. (Default is ',')
# To specify 'python engine need to be used , use 'engine' attribute.
# df = pd.read_csv('data.csv', sep= '/t', engine= 'python') #   (for tab-seperated file)

# if the dataframe index need to be start from certain index , we need to use 'header' attribute.(Default is '0')
# df = pd.read_csv('data.csv', header = None)

# if the columName of the csv file to be given explicitly we use names attributes.
# df = pd.read_csv('data.csv', names=['Duration', 'Pulse', 'Maxpulse', 'Calories'])

# if the certain column should be used as the label of the dataFrame, we need to use 'index_col' attribute.
# df = pd.read_csv('data.csv', index_col='Duration')

# if we need to create dataFrame using certain columns from the csv file , we need to use 'usecols' attribute.
# df = pd.read_csv('data.csv', usecols=['Duration', 'Pulse'])

# if the data in csv is missing to fill in that place , we need to use 'na_values' attribute.
# df = pd.read_csv('data.csv', na_values=['N/A', 'null'])

# if we need to specify the datatype of the specific column, we need to use 'dtype' attribute.
# df = pd.read_csv('data.csv', dtype={'Pulse': int})

# if we need to specify no.of rows to be read from the csv, we need to use 'nrows' attribute.
# df = pd.read_csv('data.csv', nrows=10) #(read only the first 10 rows)

# if we neeed to skip the no.of rows from begining of the csv file, we need to use 'skiprows' attribute.
# df = pd.read_csv('data.csv', skiprows=5) #(skip the first 5 rows)

print(df.to_string())
