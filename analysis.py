import pandas as pd
import numpy as np

df20 = pd.read_csv('details2020.csv')
print(df20.shape)

df20['BEGIN_MONTH'] = df20['BEGIN_YEARMONTH']%100
df20['BEGIN_YEAR'] = (df20['BEGIN_YEARMONTH']/100).astype(int)
df20 = df20.drop(columns = ['BEGIN_YEARMONTH'])
print(df20.shape)


# print(df20)


#print(df20)
# df20_1 = pd.DataFrame(df20)
# print(df20_1['BEGIN_YEAR'])
#print(df20['BEGIN_YEAR'])
# details dataset cleaning
# dfDetail20 = df20['']
# dfDetail20[['BEGIN_YEAR', 'BEGIN_MONTH']] = df['BEGIN_YEARMONTH'].str.split(' ', 1, expand=True)
# print(dfDetail20)
