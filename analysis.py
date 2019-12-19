import pandas as pd 
import json
from pandas.io.json import json_normalize
with open('qasa_stockholm.json', 'r') as f:

    load_data = json.load(f)

print(load_data)
df = json_normalize(load_data['coords']['homes'])

print(df)
#df = pd.read_json('qasa_stockholm.json', orient='columns')
#print(df)
