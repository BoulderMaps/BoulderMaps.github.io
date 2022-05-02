import pandas as pd 
import folium
from folium.plugins import LocateControl

m = folium.Map(location=[55.192192, -1.941678])
LocateControl().add_to(m)

m.save('m.html')
print("Complete")
