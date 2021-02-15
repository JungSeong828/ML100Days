import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')
x=np.random.normal(2, 1, 75)
y=2+1.5*x+np.random.normal(0,2,75)
sns.residplot(x,y,lowess=True,color='g')

sns.distplot(x,bins=15,kde=False,rug=True)
sns.distplot(x,bins=3,kde=False,rug=True)
sns.distplot(x,bins=50,kde=False,rug=True)

sns.distplot(x,bins=15,kde=True,rug=True)
