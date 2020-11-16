
import geopandas as gpd
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import osmnx as ox

# get graphs of different infrastructure types, then combine
'''
place = 'Bristol, England'
G1 = ox.graph_from_place(place,network_type='bike', custom_filter='["highway"~"cycleway"]')
G2 = ox.graph_from_place(place,network_type='bike', custom_filter='["cycleway”~"lane”]')
G = nx.compose(G1, G2)
G_projected = ox.project_graph(G)
ox.plot_graph(G_projected)
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

    if d['route'] == 'bicycle':
        bi = True
        

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
for v in gdf['name']:
    print(v)



#561023044
#177586115s
