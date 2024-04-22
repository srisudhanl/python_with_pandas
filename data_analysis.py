import pandas as pd

df = pd.read_csv('data.csv')

#print the head documents from csv file.
print("Prints the first 5 documents:\n",df.head(),"\n") #default
print("Prints the first 30 documents:\n",df.head(30),"\n")

#print the tail documents from csv file.
print("Prints the last 5 documents:\n",df.tail(),"\n") #default
print("Prints the last 30 documents:\n",df.tail(30),"\n")

#prints the info of the csv file.
print("Prints the info of csv file:\n",df.info(),"\n")