import pygrib
import cartopy.feature as cf
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import cartopy


# Open GRIB file
gfs = pygrib.open('gfs_4_20120821_1200_000.grb2')

gfs.seek(0)
for message in gfs:
    print(message)

# Volumetric Soil Moisture Content
soil_moisture = gfs[213]  
soil_moisture.units

soil_moisture_values = soil_moisture.values

soil_moisture_values.max()
soil_moisture_values.min()
lats, lons= soil_moisture.latlons()

# Plot Map 
plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=30.,standard_parallels=(20.,20.))
ax=plt.axes(projection=proj)
ax.set_extent([-100., -85., 35., 50.])
ax.add_feature(cf.LAND)
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.STATES)
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.LAKES)
ax.add_feature(cf.LAND,color='antiquewhite')
ax.add_feature(cf.OCEAN,color='aliceblue')
ax.add_feature(cf.COASTLINE,edgecolor='lightgray')
ax.add_feature(cf.STATES,edgecolor='lightgray')
ax.add_feature(cf.BORDERS,edgecolor='lightgray')
ax.add_feature(cf.LAKES,color='aliceblue')

levels = np.linspace(0, 1.05, 10)
SM_plot = plt.contourf(lons, lats, soil_moisture_values,levels=levels,cmap='autumn',transform=ccrs.PlateCarree()) # 0.0 to 0.1m 
cbar = plt.colorbar(SM_plot, orientation='horizontal', pad=0.05)
cbar.set_label('Soil Moisture (Proportion)')

plt.title('Soil Moisture')
plt.savefig('SM_plot.png', dpi=300, bbox_inches='tight')
plt.show()



