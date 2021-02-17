import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

df_r=pd.read_csv('winequality_red.csv')
df_w=pd.read_csv('winequality_white.csv')
df_r['color']='r'
df_w['color']='w'
df=pd.concat([df_r,df_w],axis=0)

df.hist(bins=10,color='lightblue',edgecolor='blue',linewidth=1.0,xlabelsize=8,ylabelsize=8,grid=False)

b=sns.heatmap(df.corr(),annot=True,linewidth=0.95)

a=sns.jointplot('fixed acidity','citric acid',data=df,kind='reg',color=None)
b=sns.jointplot('alcohol','citric acid',data=df,kind='reg')
c=sns.jointplot('volatile acidity','citric acid',data=df,kind='reg')

p=sns.catplot(x='quality',y='sulphates',kind='swarm',data=df)

sns.set(style='white')
g=sns.PairGrid(df,diag_sharey=False)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot,colors='C0')
g.map_diag(sns.kdeplot,lw=2)
