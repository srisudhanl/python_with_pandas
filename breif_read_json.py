import pandas as pd

df = pd.read_json('opendata.json')

# if file present in some other location.
# df = pd.read_json('<full_file_path_of_file>')

# if we need to specify the orientation of data in json file , we need to use 'orient' attribute.
# There are five types of orient. They are:
# => split - JSON data is split into an array of objects, and each object becomes a row in the DataFrame. (Default)
# => records - JSON data is an array of objects, and each object becomes a row in the DataFrame.
# => index - JSON data is an object where the keys are the DataFrame's row labels, and the values are the data.
# => columns - JSON data is an object where the keys are the DataFrame's column names, and the values are the data.
# => values - JSON data is just a flat list of values, which will be used as the DataFrame's single column.
# df = pd.read_json('opendata.json', orient='records')

# if we need to specify the type of the objrct to be created, we need to use 'typ' attribute.
# There are two types of typ. They are:
# => frame - Create a DataFrame.(Default)
# => series - Create a Series.
# df = pd.read_json('opendata.json', typ='series')

# if we need to convert the date-like strings to datetime objects, we use 'convert_dates' attribute.
# df = pd.read_json('opendata.json', convert_dates=True)

# if we need to convert the row labels or column labels to strings or numbers, we use 'convert_axes' attribute.
# df = pd.read_json('opendata.json', convert_axes=False)

# if we need to specifies whether to keep the default date(time) format or raise an error if the data is not in the expected format, we use 'keep_default_dates' attribute.
# df = pd.read_json('opendata.json', keep_default_dates=False)

# if we need to specifies whether to use high-precision float values, we use 'precise_float' attribute.
# df = pd.read_json('opendata.json', precise_float=True)

# if we need to specifies the unit of the date(time) data, we use 'date_unit' attribute.
# df = pd.read_json('opendata.json', date_unit='s') #(for seconds)

# if we need to specifies whether to read the JSON data as line-delimited JSON, we use 'lines' attribute.
# df = pd.read_json('opendata.json', lines=False)

print(df.to_string())
