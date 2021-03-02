#randomly assigning new cycle infrastructure#
from analysis import *
import random
G = ox.io.load_graphml('Graphall')



n = 2000

edges = list(G.edges)
i = len(edges)
non_cyc = []
G_copy = G.copy()
edge_index = []
node_list = list(G_copy.nodes)
cycmat = np.zeros((len(node_list),len(node_list)))
#identify index of non cycle lanes
for u,v,k,d in G_copy.edges(keys=True, data=True):
    bi = False
    if "bicycle" in d: #kind of uggly but not every edge has the bicycle tag
        if d['bicycle']=='designated':
            bi = True

    if d['highway']=='cycleway':
        pass


    elif 'cycleway' in d:
        pass
    elif bi:
        pass
    else:
        non_cyc.append([u,v])

print(len(non_cyc))

for k in np.random.choice(len(non_cyc),2000):
    edge = non_cyc[k]

    G_copy.edges[(edge[0],edge[1],0)]['highway'] = 'cycleway'


ox.io.save_graphml(G_copy, filepath='Graphpostupgrade_random', gephi=False, encoding='utf-8')
