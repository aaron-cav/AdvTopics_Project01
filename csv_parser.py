import pandas as pd
import numpy as np
import seaborn as se

df = pd.read_csv('auto-mpg.csv')
df.head()
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', None)
print(df.head())
car_names = df['car name'].tolist()
df['type'] = [1 if 'diesel' in element else 0 for element in car_names]
df.head()
df.pop('car name')
print(df ['type'].value_counts())

#print("Presence of null values:" + str(df.isnull().values.any()))

'''import csv

file = open('expense_profits.csv')

csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)

rows = []
for row in csvreader:
    rows.append(row)
    print(rows)'''

"""import pandas as pd

df = pd.read_csv('auto-mpg.csv')
#df.to_csv('data.csv')
print(df)"""

'''import matplotlib.pyplot as plt
import pandas as pd

# Initialize the lists for X and Y
data = pd.read_csv('auto-mpg.csv')

df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Plot the data using bar() method
plt.bar(X, Y, color='r')
plt.title("money spent on advs vs revenue")
plt.xlabel("money spent")
plt.ylabel("revenue")

# Show the plot
plt.show()'''