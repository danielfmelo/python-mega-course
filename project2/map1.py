import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])


map = folium.Map(location=[38.58, -99.09], zoom_start=8, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
	fg.add_child(folium.Marker(location=[lt, ln], popup=str(el), icon=folium.Icon(color='green')))
	map.add_child(fg)

map.save("Map1.html")

