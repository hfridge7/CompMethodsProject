# Meteogram from Metpy
import datetime as dt
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
from metpy.calc import dewpoint_from_relative_humidity
from metpy.units import units
import pandas as pd

## Missouri
def parse_date(date_str):
    return dt.datetime.strptime(date_str, "%Y-%m-%d")


def load_txt_file(filename):
    data = np.genfromtxt(
        filename, delimiter=",", names=True, dtype=None, encoding="utf-8",
        converters={"day": parse_date}
    )
    return data["day"], data[2]  


class Meteogram:
    def __init__(self, fig, dates, probeid):
        self.fig = fig
        self.dates = mpl.dates.date2num(dates)
        self.start = self.dates[0]
        self.end = self.dates[-1]
        self.probeid = probeid

    def plot_thermo(self, temp_f, dewpoint_f, plot_range=None):
        ymin, ymax, ystep = plot_range if plot_range else (10, 120, 5)
        ax = self.fig.add_subplot(2, 1, 1)
        ln1 = ax.plot(self.dates, temp_f, 'r-', label='Temperature')
        ax.fill_between(self.dates, temp_f, dewpoint_f, color='r', alpha=0.3)
        ln2 = ax.plot(self.dates, dewpoint_f, 'g-', label='Dewpoint')
        ax.fill_between(self.dates, dewpoint_f, ymin, color='g', alpha=0.3)
        ax.set_ylabel('Temperature (°F)')
        ax.set_ylim(ymin, ymax)
        ax.yaxis.set_major_locator(MultipleLocator(ystep))
        ax.grid(True)
        ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m-%d'))
        ax.legend(loc='upper left')

    def plot_rh(self, rh, plot_range=None):
        ymin, ymax, ystep = plot_range if plot_range else (0, 100, 10)
        ax = self.fig.add_subplot(2, 1, 2)
        ax.plot(self.dates, rh, 'b-', label='Relative Humidity')
        ax.fill_between(self.dates, rh, ymin, color='b', alpha=0.3)
        ax.set_ylabel('RH (%)')
        ax.set_ylim(ymin, ymax)
        ax.yaxis.set_major_locator(MultipleLocator(ystep))
        ax.grid(True)
        ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m-%d'))
        ax.legend(loc='upper left')


# Load data
temp_vals = pd.read_csv("max_temp_MO.txt", parse_dates=["day"])
rh_vals = pd.read_csv("RH_MO.txt", parse_dates=["day"])

# Align data on date (inner join)
merged = pd.merge(temp_vals, rh_vals, on=["station", "day"])

# Extract values
temp_f = merged["max_temp_f"].values * units.degF
rh = merged["avg_rh"].values / 100.0  # Convert RH to ratio

# Compute dewpoint
td = dewpoint_from_relative_humidity(temp_f.to(units.degC), rh)

# Create the meteogram
fig = plt.figure(figsize=(15, 10))
meteogram = Meteogram(fig, merged["day"].values, "Custom Station")
meteogram.plot_thermo(temp_f.magnitude, td.magnitude)
meteogram.plot_rh(merged["avg_rh"].values)  # Plot RH in percentage

fig.subplots_adjust(hspace=0.4)
plt.savefig('MO_Meteogram.png', dpi=300, bbox_inches='tight')
plt.show()

## Iowa
def parse_date(date_str):
    return dt.datetime.strptime(date_str, "%Y-%m-%d")


def load_txt_file(filename):
    data = np.genfromtxt(
        filename, delimiter=",", names=True, dtype=None, encoding="utf-8",
        converters={"day": parse_date}
    )
    return data["day"], data[2]  


class Meteogram:
    def __init__(self, fig, dates, probeid):
        self.fig = fig
        self.dates = mpl.dates.date2num(dates)
        self.start = self.dates[0]
        self.end = self.dates[-1]
        self.probeid = probeid

    def plot_thermo(self, temp_f, dewpoint_f, plot_range=None):
        ymin, ymax, ystep = plot_range if plot_range else (10, 120, 5)
        ax = self.fig.add_subplot(2, 1, 1)
        ln1 = ax.plot(self.dates, temp_f, 'r-', label='Temperature')
        ax.fill_between(self.dates, temp_f, dewpoint_f, color='r', alpha=0.3)
        ln2 = ax.plot(self.dates, dewpoint_f, 'g-', label='Dewpoint')
        ax.fill_between(self.dates, dewpoint_f, ymin, color='g', alpha=0.3)
        ax.set_ylabel('Temperature (°F)')
        ax.set_ylim(ymin, ymax)
        ax.yaxis.set_major_locator(MultipleLocator(ystep))
        ax.grid(True)
        ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m-%d'))
        ax.legend(loc='upper left')

    def plot_rh(self, rh, plot_range=None):
        ymin, ymax, ystep = plot_range if plot_range else (0, 100, 10)
        ax = self.fig.add_subplot(2, 1, 2)
        ax.plot(self.dates, rh, 'b-', label='Relative Humidity')
        ax.fill_between(self.dates, rh, ymin, color='b', alpha=0.3)
        ax.set_ylabel('RH (%)')
        ax.set_ylim(ymin, ymax)
        ax.yaxis.set_major_locator(MultipleLocator(ystep))
        ax.grid(True)
        ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m-%d'))
        ax.legend(loc='upper left')


# Load data
temp_vals = pd.read_csv("max_temp_IA.txt", parse_dates=["day"])
rh_vals = pd.read_csv("RH_IA.txt", parse_dates=["day"])

# Align data on date (inner join)
merged = pd.merge(temp_vals, rh_vals, on=["station", "day"])

# Extract values
temp_f = merged["max_temp_f"].values * units.degF
rh = merged["avg_rh"].values / 100.0  # Convert RH to ratio

# Compute dewpoint
td = dewpoint_from_relative_humidity(temp_f.to(units.degC), rh)

# Create the meteogram
fig = plt.figure(figsize=(15, 10))
meteogram = Meteogram(fig, merged["day"].values, "Custom Station")
meteogram.plot_thermo(temp_f.magnitude, td.magnitude)
meteogram.plot_rh(merged["avg_rh"].values)  # Plot RH in percentage

fig.subplots_adjust(hspace=0.4)
plt.savefig('IA_Meteogram.png', dpi=300, bbox_inches='tight')
plt.show()

## Illinois 
def parse_date(date_str):
    return dt.datetime.strptime(date_str, "%Y-%m-%d")


def load_txt_file(filename):
    data = np.genfromtxt(
        filename, delimiter=",", names=True, dtype=None, encoding="utf-8",
        converters={"day": parse_date}
    )
    return data["day"], data[2]  


class Meteogram:
    def __init__(self, fig, dates, probeid):
        self.fig = fig
        self.dates = mpl.dates.date2num(dates)
        self.start = self.dates[0]
        self.end = self.dates[-1]
        self.probeid = probeid

    def plot_thermo(self, temp_f, dewpoint_f, plot_range=None):
        ymin, ymax, ystep = plot_range if plot_range else (10, 120, 5)
        ax = self.fig.add_subplot(2, 1, 1)
        ln1 = ax.plot(self.dates, temp_f, 'r-', label='Temperature')
        ax.fill_between(self.dates, temp_f, dewpoint_f, color='r', alpha=0.3)
        ln2 = ax.plot(self.dates, dewpoint_f, 'g-', label='Dewpoint')
        ax.fill_between(self.dates, dewpoint_f, ymin, color='g', alpha=0.3)
        ax.set_ylabel('Temperature (°F)')
        ax.set_ylim(ymin, ymax)
        ax.yaxis.set_major_locator(MultipleLocator(ystep))
        ax.grid(True)
        ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m-%d'))
        ax.legend(loc='upper left')

    def plot_rh(self, rh, plot_range=None):
        ymin, ymax, ystep = plot_range if plot_range else (0, 100, 10)
        ax = self.fig.add_subplot(2, 1, 2)
        ax.plot(self.dates, rh, 'b-', label='Relative Humidity')
        ax.fill_between(self.dates, rh, ymin, color='b', alpha=0.3)
        ax.set_ylabel('RH (%)')
        ax.set_ylim(ymin, ymax)
        ax.yaxis.set_major_locator(MultipleLocator(ystep))
        ax.grid(True)
        ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m-%d'))
        ax.legend(loc='upper left')


# Load data
temp_vals = pd.read_csv("max_temp_IL.txt", parse_dates=["day"])
rh_vals = pd.read_csv("RH_IL.txt", parse_dates=["day"])

# Align data on date (inner join)
merged = pd.merge(temp_vals, rh_vals, on=["station", "day"])

# Extract values
temp_f = merged["max_temp_f"].values * units.degF
rh = merged["avg_rh"].values / 100.0  # Convert RH to ratio

# Compute dewpoint
td = dewpoint_from_relative_humidity(temp_f.to(units.degC), rh)

# Create the meteogram
fig = plt.figure(figsize=(15, 10))
meteogram = Meteogram(fig, merged["day"].values, "Custom Station")
meteogram.plot_thermo(temp_f.magnitude, td.magnitude)
meteogram.plot_rh(merged["avg_rh"].values)  # Plot RH in percentage

fig.subplots_adjust(hspace=0.4)
plt.savefig('IL_Meteogram.png', dpi=300, bbox_inches='tight')
plt.show()
