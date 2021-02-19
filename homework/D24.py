from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5,5))
m=Basemap(projection='ortho',resolution=None,lat_0=50,lon_0=-100)
m.bluemarble(scale=0.5)
plt.show()

m=Basemap(projection='mill',llcrnrlat=-90,llcrnrlon=-180,urcrnrlat=90,urcrnrlon=180,resolution='c')
m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='b')
m.drawcounties(color='darkred')
plt.title('Basemap Tutorial')
plt.show()

m=Basemap(width=12000000,height=9000000,projection='lcc',resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
m.bluemarble()
plt.show()