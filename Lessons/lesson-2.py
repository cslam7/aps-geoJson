import geopandas as gpd
import matplotlib.pyplot as plt


fp = "/home/cory/geoJson-project/Lesson-2/Data/DAMSELFISH_distributions.shp"

data = gpd.read_file(fp)

# print data
# print(type(data))
# print(data.head())

# Plot and save figure for viewing
# data.plot()
# plt.savefig('test.png')

# See coordinate systems
# print(data.crs)

# Writes to Shapefile
# out = r"/home/cory/geoJson-project/Lesson-2/Data/DAMSELFISH_distributions_SELECTION.shp"
# selection = data[0:50]
# selection.to_file(out)

# Look at geometry proproty of object geometries
# print(data['geometry'].head())

selection = data[0:5]
for index, row in selection.iterrows():
    poly_area = row['geometry'].area
    print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))

data['area'] = None

# Iterate rows one at the time
for index, row in data.iterrows():
    # Update the value in 'area' column with area information at index
    data.loc[index, 'area'] = row['geometry'].area

print(data['area'].head())

# Maximum area
max_area = data['area'].max()

# Minimum area
min_area = data['area'].mean()

print("Max area: %s\nMean area: %s" % (round(max_area, 2), round(min_area, 2)))