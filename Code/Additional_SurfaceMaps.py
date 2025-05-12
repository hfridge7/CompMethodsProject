# Additional Surface Maps 
import pygrib
import cartopy.feature as cf
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import cartopy


# Start 
# Open GRIB file
gfs_start = pygrib.open('gfs_4_20120515_1200_006.grb2')
gfs_start.seek(0)
for message in gfs_start:
    print(message)
    
# Temperature
surface_temperature_start = gfs_start[218]  
surface_temperature_start.units

surface_temperature_values_start = surface_temperature_start.values
surface_temperature_F = (9/5 * (surface_temperature_values_start - 273.15)) +32

# Determine max and min
surface_temperature_F.max()
surface_temperature_F.min()

# Define Lat and Lon
lats, lons= surface_temperature_start.latlons()

# Plot Map 
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
ax.add_feature(cf.OCEAN,color='aliceblue')
ax.add_feature(cf.COASTLINE,edgecolor='lightgray')
ax.add_feature(cf.STATES,edgecolor='lightgray')
ax.add_feature(cf.BORDERS,edgecolor='lightgray')
ax.add_feature(cf.LAKES,color='aliceblue')

levels = np.linspace(55, 110, 5)
start_temperature_plot = plt.contourf(lons, lats, surface_temperature_F, levels=levels, cmap='Wistia', transform=ccrs.PlateCarree())

# Add colorbar
cbar = plt.colorbar(start_temperature_plot, orientation='horizontal', pad=0.05)
cbar.set_label('Temperature (F)')

plt.title('2 meter Temperature (F)')
plt.savefig('surface_start_temp.png', dpi=300, bbox_inches='tight')
plt.show()


# Peak 
# Open GRIB file
gfs = pygrib.open('gfs_4_20120821_1200_006.grb2')
gfs.seek(0)
for message in gfs:
    print(message)

# Temperature
surface_temperature_peak = gfs[222]  
surface_temperature_peak.units

surface_temperature_values_peak = surface_temperature_peak.values
surface_temperature_F = (9/5 * (surface_temperature_values_peak - 273.15)) +32

# Determine max and min
surface_temperature_F.max()
surface_temperature_F.min()

# Define Lat and Lon
lats, lons= surface_temperature_peak.latlons()

# Plot Map 
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
ax.add_feature(cf.OCEAN,color='aliceblue')
ax.add_feature(cf.COASTLINE,edgecolor='lightgray')
ax.add_feature(cf.STATES,edgecolor='lightgray')
ax.add_feature(cf.BORDERS,edgecolor='lightgray')
ax.add_feature(cf.LAKES,color='aliceblue')

levels = np.linspace(55, 115, 5)
peak_temperature_plot = plt.contourf(lons, lats, surface_temperature_F, levels=levels, cmap='Wistia', transform=ccrs.PlateCarree())

# Add colorbar
cbar = plt.colorbar(peak_temperature_plot, orientation='horizontal', pad=0.05)
cbar.set_label('Temperature (F)')

plt.title('2 meter Temperature (F)')
plt.savefig('surface_peak_temp.png', dpi=300, bbox_inches='tight')
plt.show()


# End 
# Open GRIB file
gfs_end = pygrib.open('gfs_4_20130625_1200_006.grb2')
gfs_end.seek(0)
for message in gfs_end:
    print(message)

# Temperature
surface_temperature_end = gfs_end[223]  
surface_temperature_end.units

surface_temperature_values_end = surface_temperature_end.values
surface_temperature_F = (9/5 * (surface_temperature_values_end - 273.15)) +32

# Determine max and min
surface_temperature_F.max()
surface_temperature_F.min()

# Define Lat and Lon
lats, lons= surface_temperature_end.latlons()

# Plot Map 
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
ax.add_feature(cf.OCEAN,color='aliceblue')
ax.add_feature(cf.COASTLINE,edgecolor='lightgray')
ax.add_feature(cf.STATES,edgecolor='lightgray')
ax.add_feature(cf.BORDERS,edgecolor='lightgray')
ax.add_feature(cf.LAKES,color='aliceblue')

levels = np.linspace(55, 120, 5)
end_pressure_plot = plt.contourf(lons, lats, surface_temperature_F, levels=levels, cmap='Wistia', transform=ccrs.PlateCarree())

# Add colorbar
cbar = plt.colorbar(end_pressure_plot, orientation='horizontal', pad=0.05)
cbar.set_label('Temperature (F)')

plt.title('2 meter Temperature (F)')
plt.savefig('surface_end.png', dpi=300, bbox_inches='tight')
plt.show()


# 500 mb plot at the peak 
geo_hgt_500 = gfs[24]

geo_hgt_500.units
geo_hgt_500_values = geo_hgt_500.values * 0.1

# Determine Max and Min
geo_hgt_500_values.max()
geo_hgt_500_values.min()

# Define Lat and Lon
lats, lons= geo_hgt_500.latlons()

# Plot Map 
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
ax.add_feature(cf.OCEAN,color='aliceblue')
ax.add_feature(cf.COASTLINE,edgecolor='lightgray')
ax.add_feature(cf.STATES,edgecolor='lightgray')
ax.add_feature(cf.BORDERS,edgecolor='lightgray')
ax.add_feature(cf.LAKES,color='aliceblue')

levels = np.arange(1750, 2200, 2)
height_plot = ax.contour(lons, lats, geo_hgt_500_values,levels=levels, colors='black',linewidths=1.5,transform=ccrs.PlateCarree())

# Title and save
plt.title('500 Geopotential Heights (dm)')
plt.savefig('500mb_peak.png', dpi=300, bbox_inches='tight')
plt.show()


