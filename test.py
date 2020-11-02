import json
import numpy as np
import matplotlib.pyplot as plt
import shapely
from shapely.geometry import Point, Polygon, LineString, GeometryCollection
import pandas as pd


def get_junctions(data):
    #finding junctions between cycle paths to build a network
    fig = plt.figure()
    ax = fig.add_subplot(111)
    nodes = []
    for feature in data['features']:
        vector = feature['geometry']['coordinates']
        if all(isinstance(x, list) for x in vector):

            newvec = [tuple(l) for l in vector]

        else:

            newvec = tuple(vector)

        ln = LineString(newvec)

    print(vector)
    print(newvec)


        #ls = LineString(vector)
    print(len(nodes))

    return 0







if __name__ == '__main__':

    with open('bristolcycle.geojson') as f:
        data = json.load(f)

    get_junctions(data)





#distance between latlong
'''
import geopy.distance

coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

print geopy.distance.vincenty(coords_1, coords_2).km
'''
