
import geopandas as gpd
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import osmnx as ox


'''
useful_tags = ox.settings.useful_tags_way + ['cycleway'] + ['bicycle'] + ['route']
ox.utils.config(use_cache=True, log_console=True, useful_tags_way=useful_tags)
G = ox.graph_from_place(query = 'Bristol, England', network_type='bike', simplify=False,  retain_all=True)

non_cyc = []
for u,v,k,d in G.edges(keys=True, data=True):
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
        non_cyc.append((u,v,k))

G.remove_edges_from(non_cyc)
#
G = ox.utils_graph.remove_isolated_nodes(G)
G = ox.simplify_graph(G)
stats = ox.stats.basic_stats(G)
#fig, ax = ox.plot_graph(G)
print(stats)
gdf = ox.graph_to_gdfs(G, nodes=False)
'''

G_all = ox.graph_from_place(query = 'Amsterdam', network_type='bike')
#fig, ax = ox.plot_graph(G_all)

ox.io.save_graphml(G_all, filepath='Graphdam', gephi=False, encoding='utf-8')




fig, ax = ox.plot_graph(G_all,node_size = 5,show=False)



plt.savefig('lpic_figs/dam_network.pdf')





#561023044
#177586115s
