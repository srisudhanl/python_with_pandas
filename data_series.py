import pandas as pd

a = [1, 2.5, "3", True, '4.5', "Howizit"]

y = pd.Series(a)
# print whole series.
print("NormalSeries of Y:\n",y,"\n")
# print certain value from series.(As same as indexing in list)
print("Y[1]:",y[1],"\n")
print("Y[3]:",y[3],"\n")
# print(y[6]) Throws error that index is not present.

# Custom indexing the series.(index list must have same length of "list a")
# index is also known as labels.(labels can also be of any datatype)
z = pd.Series(a, index=["a", "b", "c", "d", "e", "f"]);
print("Custom index series Z:\n",z,"\n")
print("Z['a']:",z["a"],"\n")
print("Z['b']:",z["b"],"\n")

noOfPagesLearnt= {
    "day1": 3,
    "day2": 5,
    "day3": 7,
    "day4": 9
}
x = pd.Series(noOfPagesLearnt)
#prints series from dictionary.
print("Series from Dict noOfPagesLearnt:\n",x,"\n")
print("Displays selective keys from dict:\n",pd.Series(noOfPagesLearnt,index=["day1","day2"]),"\n")
print("Displays not available keywords from dict:\n",pd.Series(noOfPagesLearnt,index=["day8"]),"\n")
