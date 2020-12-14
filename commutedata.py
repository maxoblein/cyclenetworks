import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
from sklearn.preprocessing import normalize

def initialiselsoa():
    df = pd.read_csv('dataset.csv')

    names = df.iloc[:,0].tolist()


    names = names[2:]

    ids = []
    for name in names:
        id = name.split(' ',1)
        ids.append(id[0])


    #print(ids)

    with open('Lower_Layer_Super_Output_Areas__December_2011__Population_Weighted_Centroids.geojson') as f:
        data = json.load(f)

    centroids = []

    for feature in data['features']:
        if feature['properties']['lsoa11cd'] in ids:

            #print(feature['geometry']['coordinates'])
            centroids.append(feature['geometry']['coordinates'])

    #have ids and their centroid coordinates which index at the same position as matrix

    m  = np.genfromtxt('flowmatrix.csv', delimiter=',')
    m[0][0] = 15
    print(np.shape(m))
    print(len(ids))
    s =0
    for j in range(263):
        s = s + m[0][j]

    print(15/s)

    normed_matrix = normalize(m, axis=1, norm='l1')

    print(normed_matrix)

    return ids, centroids, normed_matrix

#choose lsoa
