import pandas as pd
import numpy as np
from pandas import read_csv

import matplotlib.pyplot as plt

out = pd.DataFrame(read_csv('jobs.csv'))
my_series = pd.DataFrame(out)
print(my_series)

print(out['Agency'].head(10))
print(out[["Agency",'Business Title','Work Location 1']])

ax = plt.gca()
my_series.plot(kind='line',x='Agency',y='# Of Positions',ax=ax)
plt.show()

df = pd.read_csv('jobs.csv')
df['median'] = df.groupby('Salary Range From')['Salary Range To'].transform(np.median)
gb = df.groupby('Work Location')
df1 = pd.DataFrame([df.loc[gb.groups[n], 'median'].values for n in gb.groups], index=gb.groups.keys())
df1 = df1.median(axis=1)
df1.plot()
plt.show()