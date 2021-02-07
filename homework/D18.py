import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,180)
y=np.cos(x*np.pi/180)
plt.plot(x,y)
plt.show()
plt.savefig("D18.png",dpi=300,format="png")

m=np.arange(0,3*np.pi,0.1)
n=np.cos(m)
plt.plot(m,n)
plt.show()

n=1024
a=np.random.normal(0,1,n)
b=np.random.normal(0,1,n)
plt.scatter(a,b,c='r',alpha=0.8)
plt.show()