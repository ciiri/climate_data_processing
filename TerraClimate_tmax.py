import numpy as np
import xarray as xr
from pathlib import Path
import geopandas as gpd
import warnings; warnings.filterwarnings('ignore')
ds = xr.open_dataset(r"E:\GBD\TerraClimate\Tmax\TerraClimate_tmax_1990.nc")
geometries = gpd.read_file(r"E:\GBD\shapefile\region.shp")
geometries = geometries[geometries['CONTINENT'] == 'Asia']
geometries = geometries.to_crs('EPSG:4326')
geometries = geometries.geometry
ds1 = ds.rio.set_spatial_dims('lon', 'lat')
ds2 = ds1.rio.write_crs('EPSG:4326')
ds3 = ds2.rio.clip(geometries)
ds4 = ds3.mean('lon').mean('lat')
sorted_temperatures = sorted(ds4.tmax.values, reverse=True)
top_four_temperatures = sorted_temperatures[:4]
average_temperature = sum(top_four_temperatures) / len(top_four_temperatures)
print(average_temperature)