import json
import numpy as np
import matplotlib.pyplot as plt


def get_coords(data):
    ways = []


    for feature in data['features']:
        vector = feature['geometry']['coordinates']
        ways.append(vector)
    return ways






if __name__ == '__main__':

    with open('bristolcycle.geojson') as f:
        data = json.load(f)

    ways = get_coords(data)
    




#distance between latlong
'''
import geopy.distance

coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

print geopy.distance.vincenty(coords_1, coords_2).km
'''
