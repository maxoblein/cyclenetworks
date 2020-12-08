import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

df = pd.read_csv('dataset.csv')

print(df.head())

print(df.iloc[:,0])

names = df.iloc[:,0].tolist()
print(names)

names = names[2:]

ids = []
for name in names:
    id = name.split(' ',1)
    ids.append(id[0])


print(ids)

with open('Lower_Layer_Super_Output_Areas__December_2011__Population_Weighted_Centroids.geojson') as f:
    data = json.load(f)

centroids = []

for feature in data['features']:
    if feature['properties']['lsoa11cd'] in ids:

        print(feature['geometry']['coordinates'])
