from analysis import *
G = ox.io.load_graphml('Graphall')
#path, ecpath, pct_cycle, length = random_shortest_path(adjusted_network,ODoption = 'lsoa')

nodes = list(G.nodes)
A = nx.adjacency_matrix(G)
print(len(nodes))
print(A.shape)
mat = np.zeros((len(nodes),len(nodes)))
print(mat.shape)

#set up initial graph and adjusted graph
G_copy = G
adjusted = adjust_weights(G_copy,25)

#loop for however many iterations to get flows
for i in range(500):
    path, ecpath, pct_cycle, length = random_shortest_path(adjusted,ODoption = 'lsoa')
    for k in range(len(path)-1):
        edgeused = [path[k],path[k+1]]
        indices = [nodes.index(edgeused[0]),nodes.index(edgeused[-1])]
        print(indices)
