from analysis import *
from timeit import default_timer as timer
from commutedata import *



def initflow():
    G = ox.io.load_graphml('Graphmls\Graphall')


    nodes = list(G.nodes)
    mat = np.zeros((len(nodes),len(nodes)))
    print(mat.shape)

    #set up initial graph and adjusted graph
    G_copy = G

    ids, centroids, normed_matrix = initialiselsoa()

    return G_copy, nodes, mat, ids, centroids, normed_matrix

def updatemat(path,nodes,mat):
    for k in range(len(path)-1):
        edgeused = [path[k],path[k+1]]
        indices = [nodes.index(edgeused[0]),nodes.index(edgeused[-1])]
        mat[indices[0]][indices[1]] = mat[indices[0]][indices[1]] + 1

    return mat

def getflows(adjusted,nodes,flowmat,ntrips,ids = 0, centroids = 0,normed_matrix = 0,G_true=0):
    #loop for however many iterations to get flows
    for i in range(ntrips):
        path, ecpath, pct_cycle, length = random_shortest_path(adjusted,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = G_true)
        print('new path')
        flowmat = updatemat(path,nodes,flowmat)
        print('calculated')





    return flowmat

def largest_indices(ary, n):
    """Returns the n largest indices from a numpy array."""
    flat = ary.flatten()
    indices = np.argpartition(flat, -n)[-n:]
    indices = indices[np.argsort(-flat[indices])]
    return np.unravel_index(indices, ary.shape)

def upgraderoads(G,flowmat,cycmat,updated,batchsize = 1,batchno=1):
    nodes = list(G.nodes)
    edges = list(G.edges)
    inds = largest_indices(flowmat,flowmat.shape[0])
    edges = []
    for i in range(flowmat.shape[0]):
         edges.append([nodes[inds[0][i]],nodes[inds[1][i]]])
    indicator = 0

    j = 0
    while indicator != batchsize:


        bi = False
        if cycmat[nodes.index(edges[j][0])][nodes.index(edges[j][1])] !=0:
            pass


        else:
            G.edges[(edges[j][0],edges[j][1],0)]['highway'] = 'cycleway'
            cycmat[nodes.index(edges[j][0])][nodes.index(edges[j][1])] = batchno
            updated.append([G.edges[(edges[j][0],edges[j][1],0)],batchno])
            indicator = indicator + 1

        j = j+1


    return G, updated

def plot_lpic(G,ec,save = False,show = False,filepath = None):
    fig, ax = ox.plot_graph(G, node_size=0, edge_color=ec, edge_linewidth=1.5, edge_alpha=0.7,show = False)

    if show == True:
        plt.show()
    if save == True:
        plt.savefig(filepath)


def upgrade_network(E,Nt,B,w=25):

    Nb = np.floor(E/B)

    start = timer()
    G_copy, nodes, flowmat, ids, centroids, normed_matrix = initflow()
    ec = colour_edges(G_copy)

    print('no. cycle paths = ',ec.count('r'))
    print(len(ec))


    batchsize = Nb
    updated = []
# test for a few batches
    for batchno in range(B):
        print('new batch')
        adjusted,cycmat = adjust_weights(G_copy,w)



        ntrips=Nt #the number of simulated trips to get flows

        flowmat = getflows(adjusted,nodes,flowmat,ntrips, ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = G_copy)

        G_next,updated = upgraderoads(G_copy,flowmat,cycmat,updated,batchsize,batchno+1)

        G_copy = G_next



    ec = colour_edges(G_next)

    print(updated)
    print('no. cycle paths = ',ec.count('r'))

    outfile = 'Graphmls\Graphpostupgrade' + '_' + str(E)+ '_' + str(Nt) + '_' + str(B)+ '_' + str(w)

    ox.io.save_graphml(G_next, filepath=outfile, gephi=False, encoding='utf-8')

    end = timer()

    print('update time = ',(end-start)/60)

    # #for plotting highlighted graph
    # fig, ax = ox.plot_graph(G_next, node_size=0, edge_color=ec, edge_linewidth=1.5, edge_alpha=0.7,show = False)
    # ax.set_title('Graph of road network in Bristol with cycle paths highlighted', fontsize = 18)
    #
    #
    #
    # red_patch = mpatches.Patch(color='red', label='Roads with cycle paths')
    #
    # ax.legend(handles=[red_patch])
    #
    # plt.show()
