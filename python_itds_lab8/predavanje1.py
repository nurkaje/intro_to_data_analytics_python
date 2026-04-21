import seaborn as sns
import pandas as pd

tips = sns.load_dataset('tips')

#zadatak 1
print(tips.groupby('day')[['total_bill','tip']].agg(['sum','mean']))

#zadatak 2
print(tips.groupby('day')['total_bill'].sum().idxmax())

#zadatak 3
print(pd.pivot_table(tips, values='tip', index='day', columns='time', aggfunc='mean'))

#zadatak 4
