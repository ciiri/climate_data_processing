import os
import numpy as np
import xarray as xr
from pathlib import Path
import geopandas as gpd
import pandas as pd
import warnings; warnings.filterwarnings('ignore')
os.chdir(r"E:\GBD")
geometries = gpd.read_file(r"E:\GBD\region.shp")
a = geometries['regions']
b = pd.Series(a).unique()
for i in b:
    geometries = gpd.read_file(r"E:\GBD\region.shp")
    geometries = geometries[geometries['regions'] == i]
    geometries = geometries.to_crs('EPSG:4326')
    geometries = geometries.geometry
    filePath = r"E:\GBD\cmip6\CMCC-ESM2"
    for j in os.listdir(filePath):
        os.chdir(r"E:\GBD\cmip6\CMCC-ESM2")
        ds = xr.open_dataset(j)
        tas = ds['tas'].sel(time=slice('2021', '2100'))
        tas_month = tas.groupby('time.month').mean(dim='time')
        ds1 = tas_month.rio.set_spatial_dims('lon', 'lat')
        ds2 = ds1.rio.write_crs('EPSG:4326')
        ds2['lon'] = ds2['lon'] - 180
        ds3 = ds2.rio.clip(geometries)
        ds4 = ds3.mean('lon').mean('lat')
        sorted_temperatures = sorted(ds4.values, reverse=True)
        top_four_temperatures = sorted_temperatures[:4]
        average_temperature = sum(top_four_temperatures) / len(top_four_temperatures)
        print(average_temperature - 273.15)
os.chdir(r"E:\0MD\4article\20240127GBD")



