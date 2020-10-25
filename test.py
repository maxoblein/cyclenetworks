import json
import numpy as np
import matplotlib.pyplot as plt


with open('bristolcycle.geojson') as f:
    data = json.load(f)

for feature in data['features']:
    if feature['id'] == 'way/484111801':
        print(feature['geometry']['type'])
        print(feature['geometry']['coordinates'])
        vector = feature['geometry']['coordinates']
