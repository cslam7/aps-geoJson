import geopandas as gpd
import matplotlib.pyplot as plt

# import xyzservices.providers as xyz
from bokeh.plotting import figure, save, show, output_file
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.tile_providers import get_provider, Vendors


# output_file("tile.html")
# instance = get_provider(Vendors.CARTODBPOSITRON)
# # range bounds supplied in web mercator coordinates
# p = figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000),
#            x_axis_type="mercator", y_axis_type="mercator")
# p.add_tile(instance)
# show(p)
# Save the figure as png file with resolution of 300 dpi
# outfp = r"/home/cory/geoJson-project/test-plot1.png"
# plt.savefig(outfp, dpi=300)
# exit(0)
# Filepaths
# grid_fp = r"/home/cory/geoJson-project/gz_2010_us_040_00_500k.json"
# hs_fp = r"/home/cory/geoJson-project/sps_attendance_area_HS.geojson"
# ms_fp = r"/home/cory/geoJson-project/sps_attendance_area_MS.geojson"

# # Read files
# grid = gpd.read_file(grid_fp)
# hs = gpd.read_file(hs_fp)
# ms = gpd.read_file(ms_fp)

# # Get the CRS of the grid
# gridCRS = grid.crs

# # Reproject geometries using the crs of travel time grid
# hs['geometry'] = hs['geometry'].to_crs(crs=gridCRS)
# ms['geometry'] = ms['geometry'].to_crs(crs=gridCRS)


# print(grid.head())

exit(0)
# Visualize the travel times into 9 classes using "Quantiles" classification scheme
# Add also a little bit of transparency with `alpha` parameter
# (ranges from 0 to 1 where 0 is fully transparent and 1 has no transparency)
my_map = grid.plot(column="car_r_t", linewidth=0.03, cmap="Reds", scheme="quantiles", k=9, alpha=0.9)

# Add roads on top of the grid
# (use ax parameter to define the map on top of which the second items are plotted)
hs.plot(ax=my_map, color="grey", linewidth=1.5)

# Add metro on top of the previous map
ms.plot(ax=my_map, color="red", linewidth=2.5)

# Remove the empty white-space around the axes
plt.tight_layout()

# Save the figure as png file with resolution of 300 dpi
outfp = r"/home/cory/geoJson-project/test-plot1.png"


exit(0)
# plt.savefig(outfp, dpi=300)
# # Lets try using bokeh


# # p = figure(title="My first interactive plot!")

# # print(p)

# # # Create coordinates
# # x_coords = [0, 1, 2, 3, 4]
# # y_coords = [5, 4, 1, 2, 0]
# # p.circle(x=x_coords, y=y_coords, size=10, color="red")
# # outfp = r"/home/cory/geoJson-project/Lessons/lesson-5-plot2.html"

# # save(obj=p, filename=outfp)

# # Plot shapefile interactively using bokeh
# # File path
# points_fp = r"/home/cory/geoJson-project/Lessons/Data/addresses.shp"

# # Read the data
# points = gpd.read_file(points_fp)
# # print(points.head())

# def getPointCoords(row, geom, coord_type):
#     """Calculates coordinates ('x' or 'y') of a Point geometry"""
#     if coord_type == 'x':
#         return row[geom].x
#     elif coord_type == 'y':
#         return row[geom].y

# points['x'] = points.apply(getPointCoords, geom='geometry', coord_type='x', axis=1)
# points['y'] = points.apply(getPointCoords, geom='geometry', coord_type='y', axis=1)

# p_df = points.drop('geometry', axis=1).copy()

# # print(p_df.head(2))

# # Point DataSource
# psource = ColumnDataSource(p_df)

# # Initialize plot 3 using column data source
# p = figure(title='A map of address points from a Shapefile')

# # Add the points to a map from our psource
# p.circle('x', 'y', source=psource, color='red', size=10)

# # Save interactive plot
# outfp = r"/home/cory/geoJson-project/Lessons/lesson-5-plot3.html"

# save(obj=p, filename=outfp)

# # Initialize hovertool
# my_hover = HoverTool()

# # Define potential tooltip attributes
# my_hover.tooltips = [('Address of the point', '@address'), ('Id of the point', '@id')]
# p.add_tools(my_hover)

# # Save interactive plot with hovering capabilities
# outfp = r"/home/cory/geoJson-project/Lessons/lesson-5-plot4.html"

# save(obj=p, filename=outfp)
# print(p_df.head())

from bokeh.models import HoverTool
from bokeh.plotting import figure, save
\

x = list(range(10))
y1 = [3,5,3,2,6,7,4,3,6,5]
y2 = [2,5,4,6,4,3,6,4,3,2]
y3 = [5,3,8,5,3,7,5,3,8,5]

# name the hovertool with plots desired and their tooltip will pop up
hover = HoverTool(names=["foo", "bar"])

p = figure(plot_width=600, plot_height=300, tools=[hover])
p.circle(x, y1, size=10, name="foo", color='red')
p.square(x, y2, size=10, name="bar", color='blue')
p.line(x=x, y=y3, color='black')
outfp = r"/home/cory/geoJson-project/Lessons/lesson-5-hovertool.html"

save(obj=p, filename=outfp)
