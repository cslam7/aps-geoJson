import geopandas as gpd
import matplotlib.pyplot as plt
from bokeh.plotting import figure, save
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool

# Filepaths
grid_fp = r"/home/cory/geoJson-project/Lessons/Data/TravelTimes_to_5975375_RailwayStation.shp"
roads_fp = r"/home/cory/geoJson-project/Lessons/Data/roads.shp"
metro_fp = r"/home/cory/geoJson-project/Lessons/Data/metro.shp"

# Read files
grid = gpd.read_file(grid_fp)
roads = gpd.read_file(roads_fp)
metro = gpd.read_file(metro_fp)

# Get the CRS of the grid
gridCRS = grid.crs

# Reproject geometries using the crs of travel time grid
roads['geometry'] = roads['geometry'].to_crs(crs=gridCRS)
metro['geometry'] = metro['geometry'].to_crs(crs=gridCRS)

# Visualize the travel times into 9 classes using "Quantiles" classification scheme
# Add also a little bit of transparency with `alpha` parameter
# (ranges from 0 to 1 where 0 is fully transparent and 1 has no transparency)
my_map = grid.plot(column="car_r_t", linewidth=0.03, cmap="Reds", scheme="quantiles", k=9, alpha=0.9)

print(grid.head())

exit(0)
# # # Add roads on top of the grid
# # # (use ax parameter to define the map on top of which the second items are plotted)
# # roads.plot(ax=my_map, color="grey", linewidth=1.5)

# # # Add metro on top of the previous map
# # metro.plot(ax=my_map, color="red", linewidth=2.5)

# # # Remove the empty white-space around the axes
# # plt.tight_layout()

# # # Save the figure as png file with resolution of 300 dpi
# # outfp = r"/home/cory/geoJson-project/Lessons/lesson-5-plot1.png"
# # plt.savefig(outfp, dpi=300)
# # # Lets try using bokeh


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

from bokeh.plotting import output_notebook, figure, show
from bokeh.models import HoverTool
from bokeh.plotting import figure, save

# output_notebook()

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
