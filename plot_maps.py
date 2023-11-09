import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import contextily as ctx
import networkx as nx
import osmnx as ox
from shapely.geometry import Point, Polygon

# Set black background
plt.style.use('dark_background')

# Define ROI bbox
bbox = "2.340151410392309,48.8499183196836,2.3536185628854582,48.85889296844759".split(',')

# Create Polygon from bbox
poly = Polygon([(float(bbox[0]), float(bbox[1])), (float(bbox[2]), float(bbox[1])), 
                (float(bbox[2]), float(bbox[3])), (float(bbox[0]), float(bbox[3]))])

# Get graph from bbox
G = ox.graph_from_polygon(poly, network_type='all')
gdf_edges = ox.utils_graph.graph_to_gdfs(G, nodes=False, edges=True, 
                                         node_geometry=False, fill_edge_geometry=True)

# Create GeoDataFrame from BBox
gdf = gpd.GeoDataFrame(index=[0], crs="EPSG:4326", geometry=[poly])

# Plot GeoDataFrame
ax = gdf.plot(facecolor='none', linewidth=3, edgecolor='red', figsize=(10,10))

# Plot graph on top of GeoDataFrame
gdf_edges.plot(ax=ax, linewidth=2, edgecolor='red', alpha=0.5)
ax.set_axis_off()

year_map = '1892'

# Add basemap
if year_map == '1742':
    ctx.add_basemap(ax, source='Paris1742.tif', crs=gdf.crs)
elif year_map == '1804':
    ctx.add_basemap(ax, source='Paris1804.tif', crs=gdf.crs)
elif year_map == '1892':
    ctx.add_basemap(ax, source='Paris1892.tif', crs=gdf.crs)
elif year_map == '1910':
    ctx.add_basemap(ax, source='Paris1910.tif', crs=gdf.crs)
else:
    ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron, crs=gdf.crs)

# Maximize plot window
# figManager = plt.get_current_fig_manager()
# figManager.full_screen_toggle()

plt.show()
