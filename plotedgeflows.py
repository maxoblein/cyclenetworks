#script to plot edge flows on graph#
from upgrade import *
import matplotlib.cm as cm

G = ox.io.load_graphml('Graphmls/Graphall')

G_next,flowmat = upgrade_network(160000,10000,1,w=2)

print(np.max(flowmat))

numrows = flowmat.shape[0]
numcols = flowmat.shape[1]

print(numrows)
print(numcols)
nodelist = list(G.nodes)
print(len(nodelist))

for u, v, k, d in G.edges(keys = True, data=True):
    d['flow'] = flowmat[nodelist.index(u)][nodelist.index(v)]
    if flowmat[nodelist.index(u)][nodelist.index(v)] > 0:
        print(flowmat[nodelist.index(u)][nodelist.index(v)])

nodes,edges = ox.graph_to_gdfs(G, nodes=True, edges=True)
print(edges['flow'].max())
cmap = plt.cm.get_cmap('jet')
norm=plt.Normalize(vmin=edges['flow'].min(), vmax=edges['flow'].max())
sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])


ec = ox.plot.get_edge_colors_by_attr(G,'flow',cmap='jet')

fig, ax = ox.plot_graph(G, node_size=0, edge_color=ec, edge_linewidth=0.8, edge_alpha=0.7,save=False, show=False, filepath = 'lpic_figs/Graph_of_edgeflows.pdf',bgcolor='lightgray')
cb = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical')
plt.show()
# cb.set_label('shortest_route_length_to_target', fontsize = 20)
#fig.savefig('lpic_figs/edgeflows_with-colourbar.pdf')
