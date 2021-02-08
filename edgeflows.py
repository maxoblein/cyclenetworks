from analysis import *
from timeit import default_timer as timer




def initflow():
    G = ox.io.load_graphml('Graphall')


    nodes = list(G.nodes)
    mat = np.zeros((len(nodes),len(nodes)))
    print(mat.shape)

    #set up initial graph and adjusted graph
    G_copy = G


    return G_copy, nodes, mat

def updatemat(path,nodes,mat):
    for k in range(len(path)-1):
        edgeused = [path[k],path[k+1]]
        indices = [nodes.index(edgeused[0]),nodes.index(edgeused[-1])]
        mat[indices[0]][indices[1]] = mat[indices[0]][indices[1]] + 1

    return mat

def getflows(adjusted,nodes,flowmat,ntrips):
    start = timer()
    #loop for however many iterations to get flows
    for i in range(ntrips):
        print('new path')
        path, ecpath, pct_cycle, length = random_shortest_path(adjusted,ODoption = 'lsoa')

        flowmat = updatemat(path,nodes,flowmat)


    print(np.nonzero(flowmat))
    print(np.amax(flowmat))
    end = timer()
    print('update time = ',(end-start))

    return flowmat

def largest_indices(ary, n):
    """Returns the n largest indices from a numpy array."""
    flat = ary.flatten()
    indices = np.argpartition(flat, -n)[-n:]
    indices = indices[np.argsort(-flat[indices])]
    return np.unravel_index(indices, ary.shape)

def upgraderoads(G,flowmat,cycmat,batchsize = 1,batchno=1):
    nodes = list(G.nodes)
    edges = list(G.edges)
    inds = largest_indices(flowmat,flowmat.shape[0])
    print(inds)
    print(nodes[inds[1][0]])
    edges = []
    for i in range(flowmat.shape[0]):
         edges.append([nodes[inds[0][i]],nodes[inds[1][i]]])
    print(edges)
    indicator = 0
    j = 0
    while indicator != batchsize:


        bi = False
        if cycmat[nodes.index(edges[j][0])][nodes.index(edges[j][1])] !=0:
            pass


        else:
            print(G.edges[(edges[j][0],edges[j][1],0)])
            G.edges[(edges[j][0],edges[j][1],0)]['highway'] = 'cycleway'
            cycmat[nodes.index(edges[j][0])][nodes.index(edges[j][1])] = batchno
            print(G.edges[(edges[j][0],edges[j][1],0)])
            print(j)
            indicator = indicator + 1

        j = j+1


    return G



if __name__ == '__main__':


    G_copy, nodes, flowmat = initflow()
    ec = colour_edges(G_copy)

    print('no. cycle paths = ',ec.count('r'))

    #for plotting highlighted graph
    fig, ax = ox.plot_graph(G_copy, node_size=0, edge_color=ec, edge_linewidth=1.5, edge_alpha=0.7,show = False)
    ax.set_title('Graph of road network in Bristol with cycle paths highlighted', fontsize = 18)



    red_patch = mpatches.Patch(color='red', label='Roads with cycle paths')

    ax.legend(handles=[red_patch])

    plt.show()

    batchsize = 50
# test for a few batches
    for batchno in range(10):
        adjusted,cycmat = adjust_weights(G_copy,25)

        ntrips=25 #the number of simulated trips to get flows

        flowmat = getflows(adjusted,nodes,flowmat,ntrips)

        G_next = upgraderoads(G_copy,flowmat,cycmat,batchsize,batchno+1)

        G_copy = G_next



    ec = colour_edges(G_next)

    print(cycmat)
    print('no. cycle paths = ',ec.count('r'))

    #for plotting highlighted graph
    fig, ax = ox.plot_graph(G_next, node_size=0, edge_color=ec, edge_linewidth=1.5, edge_alpha=0.7,show = False)
    ax.set_title('Graph of road network in Bristol with cycle paths highlighted', fontsize = 18)



    red_patch = mpatches.Patch(color='red', label='Roads with cycle paths')

    ax.legend(handles=[red_patch])

    plt.show()
