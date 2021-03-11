#script to plot edge flows on graph#
from upgrade import *

G = ox.io.load_graphml('Graphmls/Graphall')

flowmat = upgrade_network(2000,10000,1,w=2)

print(np.max(flowmat))

numrows = flowmat.shape[0]
numcols = flowmat.shape[1]

print(numrows)
print(numcols)
nodelist = list(G.nodes)
print(len(nodelist))

for u, v, k, d in G.edges(keys = True, data=True):
    d['flow'] = flowmat[nodelist.index(u)][nodelist.index(v)]


ec = ox.plot.get_edge_colors_by_attr(G,'flow')

fig, ax = ox.plot_graph(G, node_size=0, edge_color=ec, edge_linewidth=1.5, edge_alpha=0.7,save=True, filepath = 'lpic_figs/Graph_of_edgeflows.pdf')
