import folium

map = folium.Map(location=[37, 0],
            zoom_start=2.5,
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',

        #     tiles='https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}',
            attr='My Data Attribution')


states = r"/home/cory/geoJson-project/gz_2010_us_040_00_500k.json"
# hs = r'/home/cory/geoJson-project/sps_attendance_area_HS.geojson'
# ms = r'/home/cory/geoJson-project/sps_attendance_area_MS.geojson'

state_data = folium.GeoJson(
    states,
    name='states'
).add_to(map)

# # hs_data = folium.GeoJson(
# #     hs,
# #     name='hs'
# # ).add_to(map)

# ms_data = folium.GeoJson(
#     ms,
#     name='ms'
# ).add_to(map)

folium.GeoJsonTooltip(fields=["NAME"]).add_to(state_data)
# # folium.GeoJsonTooltip(fields=["HS_ZONE"]).add_to(hs_data)
# folium.GeoJsonTooltip(fields=["MS_ZONE"]).add_to(ms_data)




map.save("/home/cory/geoJson-project/test-map.html")