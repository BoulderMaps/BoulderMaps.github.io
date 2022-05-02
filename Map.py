#from msilib.schema import Icon
from turtle import color
import folium
import pandas as pd
from folium.plugins import LocateControl

areas = pd.read_excel("Boulders.xlsx", sheet_name = "Areas")
a_lat = list(areas["LAT"])
a_lon = list(areas["LON"])
a_area = list(areas["AREA"])

boulders = pd.read_excel("Boulders.xlsx", sheet_name = "Boulders")
b_lat = list(boulders["LAT"])
b_lon = list(boulders["LON"])
b_area = list(boulders["AREA"])

parking = pd.read_excel("Boulders.xlsx", sheet_name = "Parking")
p_lat = list(parking["LAT"])
p_lon = list(parking["LON"])
p_area = list(parking["AREA"])

map = folium.Map(location=[55.129074, -1.912727])

fga = folium.FeatureGroup(name="Areas")
fgb = folium.FeatureGroup(name="Boulders")
fgp = folium.FeatureGroup(name="Parking")

for lt, ln, ar in zip(b_lat, b_lon, b_area):
    fgb.add_child(folium.Marker(location=[lt, ln], popup=str(ar), fill=True, fill_opacity=0.7))

for lt, ln, ar in zip(p_lat, p_lon, p_area):
    fgp.add_child(folium.Marker(location=[lt, ln], icon=folium.Icon(color='blue', icon='fa-car', prefix='fa'), popup=str(ar), fill=True, fill_opacity=0.7))

map.add_child(fgb)
map.add_child(fgp)

map.add_child(folium.LayerControl())

LocateControl().add_to(map)

map.save('index.html')
print("Complete")
