import os
import numpy as np
import xarray as xr
from pathlib import Path
import geopandas as gpd
import pandas as pd
import warnings; warnings.filterwarnings('ignore')
os.chdir(r"E:\GBD")
geometries = gpd.read_file(r"E:\GBD\shapefile\region.shp")
a = geometries['latitude']
b = pd.Series(a).unique()
for i in b:
    geometries = gpd.read_file(r"E:GBD\shapefile\region.shp")
    geometries = geometries[geometries['latitude'] == i]
    geometries = geometries.to_crs('EPSG:4326')
    geometries = geometries.geometry
    filePath = r"E:\GBD\TerraClimate\soil"
    for j in os.listdir(filePath):
        os.chdir(r"E:\GBD\TerraClimate\soil")
        ds = xr.open_dataset(j)
        ds1 = ds.rio.set_spatial_dims('lon', 'lat')
        ds2 = ds1.rio.write_crs('EPSG:4326')
        ds3 = ds2.rio.clip(geometries)
        ds4 = ds3.mean('time').mean('lon').mean('lat')
        print(ds4.soil.values)
os.chdir(r"E:\GBD")