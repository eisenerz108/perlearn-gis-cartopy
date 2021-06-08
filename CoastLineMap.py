"""
Created Date : 08-Jun-21
@author : Aman Jain
"""
##

import numpy as np
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature



fig = plt.figure(figsize = (10,10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.gridlines()