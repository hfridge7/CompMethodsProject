# Gridded Data
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

rh_850 = gfs[161]
temp_850 = gfs[160]

rh_850_values = rh_850.values
temp_850_values = temp_850.values - 273.15 # K to C
lats, lons = temp_850.latlons()

rh_850_values.max()
rh_850_values.min()

temp_850_values.max()
temp_850_values.min()


plt.figure(figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=30.,standard_parallels=(20.,20.))
ax=plt.axes(projection=proj)
ax.set_extent([-125.,-70.,20.,50.])
ax.add_feature(cf.LAND)
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.STATES)
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.LAKES)
ax.add_feature(cf.LAND,color='antiquewhite')
ax.add_feature(cf.OCEAN,color='cornflowerblue')
ax.add_feature(cf.COASTLINE,edgecolor='lightgray')
ax.add_feature(cf.STATES,edgecolor='lightgray')
ax.add_feature(cf.BORDERS,edgecolor='lightgray')
ax.add_feature(cf.LAKES,color='cornflowerblue')

temp_plot = ax.contour(lons, lats, temp_850_values,levels=np.arange(-40, 40, 10), cmap='cool',linewidths=1.0,linestyles='dotted',transform=ccrs.PlateCarree())

rh_plot = ax.contourf(lons, lats, rh_850_values,levels=np.arange(70, 101, 10),cmap='Greens',alpha=1.0,transform=ccrs.PlateCarree())
# Add colorbar for RH
cbar = plt.colorbar(rh_plot, ax=ax, shrink=0.7, pad=0.05, orientation='horizontal')
cbar.set_label('850 mb Relative Humidity (%)')

# Title and save
plt.title('850 Temperature (°C)/Relative Humidity (%)')
plt.savefig('850mb.png', dpi=300, bbox_inches='tight')
plt.show()
