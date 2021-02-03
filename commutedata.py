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

    #remove in lsoa movement

    for i in range(m.shape[0]):
        m[i][i] = 0


    normed_matrix = normalize(m, axis=1, norm='l1')

    s = 0
    for j in range(normed_matrix.shape[0]):
        s = s + normed_matrix[0][j]

    

    return ids, centroids, normed_matrix

#choose lsoa
