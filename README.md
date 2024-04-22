# PYTHON WITH PANDAS

***

## Prelims:

***
> Install PYTHON latest version on your system.
>
> Tutorial Link: https://youtu.be/nhv82tvFfkM?si=FPccuGL4s1_57iWe

> Install PYCHARM latest version on your system for easy computation.
>
> Tutorial Link: https://youtu.be/ZVjQFjOI49c?si=kk8Je--TbzHocsVx

### First Program: [intro](intro.py)

***

* Prints the directories in `pandas` library.
* Prints the dictionary as `dataframe` in `pandas`.
* Prints the type of variable that consist of `dataFrame` object.
* Prints the `version of pandas`.

### Second Program: [Data_Series](data_series.py)

***

* Prints the series of data using `Series()`.
* Prints the certain value in series using index which is called as `label` in pandas.
* Both `labels` and `values` can be of any data type and can be mapped to any other data type or same.
* So, we can also give `custom labels value` for the series.
* We can convert the `JSON` data as series or interpretable structure using `Series()`.
* When we request for the value of the key in the series, if that is not present within the series, it returns `NaN`
  value.

### Third Program: [Data Frame](data_frame.py)

***

* Prints the DataFrame using `DataFrame()`.
* Prints the certain data from the DataFrame using `loc[<index_value>]` method.
* Prints more than one data from the DataFrame using `loc[<list_of_index_values>]` method.
* Prints the Dataframe with `custom_indexes`.
* Prints the certain data using custom index.
* Prints more than one data from the dataframe using custom_indexes.

### Fourth Program: [Read Data From CSV/JSON](reading_data_from_csv_json.py)

***

* Reads the data from csv file using `.read_csv()`.
* Prints the read_data in dataframe object.
* Prints the read_data in string object.
* Reads the data from JSON file using `.read_json()`.
* Prints the read_data in dataframe object.
* Prints the read_data in string object.
* We can also verify the type using `type()`.
* If file is present in any other location, use file path to read that file.

### Fifth Program: [Brief About read_csv()](breif_read_csv.py)

***

* To know Brief about `read_csv()` refer the program.

### Sixth Program: [Brief About read_json()](breif_read_json.py)

***

* To know Brief about `read_json()` refer the program.

### Seventh Program: [Head/ Tail documents](data_analysis.py)

***

* To display first and last documents using `head()` and `tail()`.

### Eighth Program: [Data cleaning/ Data Replacing](data_cleaning.py)

***

* To clean the null or not present data we use `dropna()` and `dropna(inplace=True)`.
* To replace the null or not present data we use `fillna(<replace_term>)` and `fillna(<replace_term>,inplace=True)`.
* We can also seperate fill values for each columns seperately.

### Nineth Program: [Mean / Median / Mode](mean_median_mode.py)

***

* We can get the mean value of all numerical column or certain numerical column using `mean()`.
* We can get the median value of all numerical column or certain numerical column using `median()`.
* We can get the mode value of all numerical column or certain numerical column using `mode()`.
* `mode()` returns the array as output which consist of mode of each column given for computation.

### Tenth Program: [Data Reformatting](data_reformatting.py)

***

* We can format the date that present in column using to_datetime() and we need to give the format.
* We can add 'errors' attribute if there is no value in certain row given column.
* We can also iterate throughout the data file using for loop.

### Eleventh Program: [Remove Duplicates](remove_duplicate_data.py)

***

* We can find whether the row is duplicate or not by using `duplicated()`.
* It returns true if it is duplicated, and returns false it is not duplicated.
* We can drop the duplicate rows from the dataframe using `drop_duplicates()`.

### Twelveth Program: [Write data to CSV/JSON](save_cleaned_files.py)

***

* We can save the dataframe to csv by using `to_csv(<fileName>)`.
* We can save the dataframe to json by using `to_json(<filename>)`.

### Thirteenth Program: [Data Correlation](data_correlation.py)

***

* It is used to find the correlation between the data present in each column.
* Data Correlation is measured in the scale of `-1 to 1`.
* Data is said to be good data if the data correlation is between `0.5 to 0.9`.