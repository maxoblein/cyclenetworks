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

xcoord = np.ones(len(vector))
ycoord = np.ones(len(vector))

for i in range(len(vector)):
    xcoord[i] = vector[i][0]
    ycoord[i] = vector[i][1]


print(xcoord)
print(ycoord)
#fig = plt.figure()
#ax =  fig.add_subplot(111)
#ax.plot(xcoord,ycoord)
#plt.show()
