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

def getflows(adjusted,nodes,mat,ntrips):
    start = timer()
    #loop for however many iterations to get flows
    for i in range(ntrips):
        print('new path')
        path, ecpath, pct_cycle, length = random_shortest_path(adjusted,ODoption = 'lsoa')

        mat = updatemat(path,nodes,mat)


    print(np.nonzero(mat))
    print(np.amax(mat))
    end = timer()
    print('update time = ',(end-start))

def largest_indices(ary, n):
    """Returns the n largest indices from a numpy array."""
    flat = ary.flatten()
    indices = np.argpartition(flat, -n)[-n:]
    indices = indices[np.argsort(-flat[indices])]
    return np.unravel_index(indices, ary.shape)

def upgraderoads(G,mat,nstreets = 1):
    nodes = list(G.nodes)
    edges = list(G.edges)
    inds = largest_indices(mat,mat.shape[0])
    print(inds)
    print(nodes[inds[1][0]])
    edges = []
    for i in range(mat.shape[0]):
         edges.append([nodes[inds[0][i]],nodes[inds[1][i]]])
    print(edges)
    indicator = 0
    j = 0
    while indicator != nstreets:


        bi = False
        if "bicycle" in G.edges[(edges[j][0],edges[j][1],0)]: #kind of uggly but not every edge has the bicycle tag
            if G.edges[(edges[j][0],edges[j][1],0)]["bicycle"] == 'designated':
                bi = True

        if G.edges[(edges[j][0],edges[j][1],0)]['highway']=='cycleway':
            pass


        elif 'cycleway' in G.edges[(edges[j][0],edges[j][1],0)]:
            pass
        elif bi:
            pass
        else:
            print(G.edges[(edges[j][0],edges[j][1],0)])
            G.edges[(edges[j][0],edges[j][1],0)]['highway'] = 'cycleway'
            print(G.edges[(edges[j][0],edges[j][1],0)])
            print(j)
            indicator = indicator + 1

        j = j+1


    return G



if __name__ == '__main__':


    G_copy, nodes, mat = initflow()
    adjusted = adjust_weights(G_copy,25)

    ntrips=10 #the number of simulated trips to get flows

    getflows(adjusted,nodes,mat,ntrips)

    G_next = upgraderoads(G_copy,mat,5)
