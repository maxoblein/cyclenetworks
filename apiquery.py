import osmnx as ox
useful_tags = ox.settings.useful_tags_way + ['cycleway']
ox.config(use_cache=True, log_console=True, useful_tags_way=useful_tags)
G = ox.graph_from_place(query = 'Bristol, England', network_type='bike', simplify=False)
non_cycleways = [(u, v, k) for u, v, k, d in G.edges(keys=True, data=True) if not ('cycleway' in d or d['highway']=='cycleway')]
G.remove_edges_from(non_cycleways)
G = ox.utils_graph.remove_isolated_nodes(G)
G = ox.simplify_graph(G)
fig, ax = ox.plot_graph(G)
