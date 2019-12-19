import pandas as pd 
import json
from pandas.io.json import json_normalize
import os
import gmaps
from ipywidgets.embed import embed_minimal_html
from ipywidgets.embed import embed_data
with open('qasa_stockholm.json', 'r') as f:
    load_data = json.load(f)
df = json_normalize(load_data['coords']['homes'])

print(df)
print(df.sort_values(by='cost'))
df = df[df['cost']>=100]
print(df.sort_values(by='cost'))
print(df.sort_values(by='currency'))
#gmaps.configure(api_key=os.environ['gmaps_API']) # Fill in with your API key
m = gmaps.Map()
df['latitude'] = df['latitude'].astype(float)
df['longitude'] = df['longitude'].astype(float)
df['cost'] = df['cost'].astype(float)
heatmap_layer = gmaps.heatmap_layer(df[['latitude','longitude']], weights=df['cost'],max_intensity=25000, point_radius=5.0)
m.add_layer(heatmap_layer)
embed_minimal_html('export.html', views=[m])
