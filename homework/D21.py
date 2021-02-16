import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df=sns.load_dataset('titanic')
df.info

sns.barplot(x='sex',y='survived',hue='class',data=df)
plt.show()

g=sns.FacetGrid(df,col='survived')
g.map(plt.hist,'sex')
plt.show()

h=sns.FacetGrid(df,col='survived')
h.map(plt.hist,'pclass')
plt.show()

survived=df.groupby(['pclass','sex']).survived.sum()
survived.plot(kind='bar')

counts=pd.crosstab([df.pclass,df.sex],df.survived)
counts
counts.plot(kind='bar',stacked=True)

sns.violinplot(data=counts)
plt.show()