import pandas as pd 
import folium
from folium.plugins import LocateControl

m = folium.Map(location=[45.5236, -1.6750])
LocateControl().add_to(m)

m.save('m.html')
print("Complete")
