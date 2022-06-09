import pandas as pd

my_series = pd.Series([5,6,7,8,9,10])
#print(my_series)
#print(my_series.index)
#print(my_series[2])

my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'f', 'g'])
#print(my_series2[['a', 'b', 'c']])
my_series2[['a', 'b', 'c']] = 11
#print(my_series2)
my_series2[my_series2 < 11] *= 2
#print(my_series2)

my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7})
print(my_series3)
my_series3.name = 'numbers'
my_series3.index.name = 'letters'
print(my_series3)


