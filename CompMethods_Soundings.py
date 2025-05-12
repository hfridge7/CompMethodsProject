import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
from siphon.simplewebservice.wyoming import WyomingUpperAir
from datetime import datetime

# Sounding from Metpy
## Missouri 
### During Peak
dt = datetime(2012, 8, 21, 12) # define date and time
station = 'SGF'

df_MO_Sounding = WyomingUpperAir.request_data(dt, station)

data_MO_Sounding = pandas_dataframe_to_unit_arrays(df_MO_Sounding)

# Variables and units
p_MO_Sounding =data_MO_Sounding['pressure']
T_MO_Sounding = data_MO_Sounding['temperature']
Td_MO_Sounding = data_MO_Sounding['dewpoint']
u_MO_Sounding = data_MO_Sounding['u_wind']
v_MO_Sounding = data_MO_Sounding['v_wind']

fig_MO_Sounding = plt.figure(figsize=(9,11))
skew_MO = SkewT(fig_MO_Sounding, rotation=45)

skew_MO.plot(p_MO_Sounding, T_MO_Sounding, 'r')
skew_MO.plot(p_MO_Sounding, Td_MO_Sounding, 'g')
skew_MO.plot_barbs(p_MO_Sounding[::3], u_MO_Sounding[::3], v_MO_Sounding[::3], y_clip_radius=0.03)

skew_MO.ax.set_xlabel('Temperature (\N{DEGREE CELSIUS})')
skew_MO.ax.set_ylabel('Pressure (mb)')

plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');

skew_MO.plot_dry_adiabats()
skew_MO.plot_moist_adiabats()
skew_MO.plot_mixing_lines()
skew_MO.ax.set_ylim(1000, 100)

plt.savefig('MO_Sounding.png', dpi=300, bbox_inches='tight')
plt.show()

## Iowa
### During Peak
dt = datetime(2012, 8, 21, 12) # define date and time
station = 'DVN'

df_IA_Sounding = WyomingUpperAir.request_data(dt, station)

data_IA_Sounding = pandas_dataframe_to_unit_arrays(df_IA_Sounding)

# Variables and units
p_IA_Sounding =data_IA_Sounding['pressure']
T_IA_Sounding = data_IA_Sounding['temperature']
Td_IA_Sounding = data_IA_Sounding['dewpoint']
u_IA_Sounding = data_IA_Sounding['u_wind']
v_IA_Sounding = data_IA_Sounding['v_wind']

fig_IA_Sounding = plt.figure(figsize=(9,11))
skew_IA = SkewT(fig_IA_Sounding, rotation=45)

skew_IA.plot(p_IA_Sounding, T_IA_Sounding, 'r')
skew_IA.plot(p_IA_Sounding, Td_IA_Sounding, 'g')
skew_IA.plot_barbs(p_IA_Sounding[::3], u_IA_Sounding[::3], v_IA_Sounding[::3], y_clip_radius=0.03)

skew_IA.ax.set_xlabel('Temperature (\N{DEGREE CELSIUS})')
skew_IA.ax.set_ylabel('Pressure (mb)')

plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');

skew_IA.plot_dry_adiabats()
skew_IA.plot_moist_adiabats()
skew_IA.plot_mixing_lines()
skew_IA.ax.set_ylim(1000, 100)

plt.savefig('IA_Sounding.png', dpi=300, bbox_inches='tight')
plt.show()

## Illinois (KILX)
### During Peak
dt = datetime(2012, 8, 21, 12) # define date and time
station = 'ILX'

df_IL_Sounding = WyomingUpperAir.request_data(dt, station)

data_IL_Sounding = pandas_dataframe_to_unit_arrays(df_IL_Sounding)

# Variables and units
p_IL_Sounding = data_IL_Sounding['pressure']
T_IL_Sounding = data_IL_Sounding['temperature']
Td_IL_Sounding = data_IL_Sounding['dewpoint']
u_IL_Sounding = data_IL_Sounding['u_wind']
v_IL_Sounding = data_IL_Sounding['v_wind']

fig_IL_Sounding = plt.figure(figsize=(9,11))
skew_IL = SkewT(fig_IL_Sounding, rotation=45)

skew_IL.plot(p_IL_Sounding, T_IL_Sounding, 'r')
skew_IL.plot(p_IL_Sounding, Td_IL_Sounding, 'g')
skew_IL.plot_barbs(p_IL_Sounding[::3], u_IL_Sounding[::3], v_IL_Sounding[::3], y_clip_radius=0.03)

skew_IL.ax.set_xlabel('Temperature (\N{DEGREE CELSIUS})')
skew_IL.ax.set_ylabel('Pressure (mb)')

plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(dt), loc='right');

skew_IL.plot_dry_adiabats()
skew_IL.plot_moist_adiabats()
skew_IL.plot_mixing_lines()
skew_IL.ax.set_ylim(1000, 100)

plt.savefig('IL_Sounding.png', dpi=300, bbox_inches='tight')
plt.show()
