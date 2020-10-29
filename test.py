import json
import numpy as np
import matplotlib.pyplot as plt


with open('bristolcycle.geojson') as f:
    data = json.load(f)

ways = []


for feature in data['features']:
    vector = feature['geometry']['coordinates']
    ways.append(vector)

print(len(ways))


#distance between latlong
'''
import geopy.distance

coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

print geopy.distance.vincenty(coords_1, coords_2).km
'''
