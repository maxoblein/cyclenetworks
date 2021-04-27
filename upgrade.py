from analysis import *
from timeit import default_timer as timer
from commutedata import *
import matplotlib.cm as cm
import matplotlib as mpl
import matplotlib.pylab as plb


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
    while indicator <= batchsize:


        bi = False
        if cycmat[nodes.index(edges[j][0])][nodes.index(edges[j][1])] !=0:
            pass


        else:
            G.edges[(edges[j][0],edges[j][1],0)]['highway'] = 'cycleway'
            #indicate the batch in which upgraded
            G.edges[(edges[j][0],edges[j][1],0)]['batch'] = batchno
            cycmat[nodes.index(edges[j][0])][nodes.index(edges[j][1])] = batchno
            updated.append([G.edges[(edges[j][0],edges[j][1],0)],batchno])
            indicator = indicator + G.edges[(edges[j][0],edges[j][1],0)]['length']

        j = j+1


    return G, updated

def plot_lpic(G,ec,save = False,show = False,filepath = None):
    fig, ax = ox.plot_graph(G, node_size=0, edge_color=ec, edge_linewidth=1.5, edge_alpha=0.7,show = False)

    if show == True:
        plt.show()
    if save == True:
        plt.savefig(filepath)


def upgrade_network(L,Nt,B,w=2,savebatch = False,save=False):

    Nb = L/B

    start = timer()
    G_copy, nodes, flowmat, ids, centroids, normed_matrix = initflow()
    ec = colour_edges(G_copy)

    print('no. cycle paths = ',ec.count('r'))
    print(len(ec))
    outfile = 'Graphmls\Graphpostupgrade' + '_' + str(L)+ '_' + str(Nt) + '_' + str(B) + '_' + str(w)

    #add batch tag to edges to track when upgraded

    for u,v,k,d in G_copy.edges(keys=True,data=True):
        d['batch'] = 0

    batchsize = Nb
    updated = []
# test for a few batches
    for batchno in range(B):
        print('new batch')
        adjusted,cycmat = adjust_weights(G_copy,w)



        ntrips=Nt #the number of simulated trips to get flows

        flowmat = getflows(adjusted,nodes,flowmat,ntrips, ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = G_copy)

        G_next,updated = upgraderoads(G_copy,flowmat,cycmat,updated,batchsize,batchno+1)

        if savebatch == True:
            batchout = 'Graphmls/batches_2000_w2/batch_' + str(batchno)
            ox.io.save_graphml(G_next, filepath=batchout , gephi=False, encoding='utf-8')

        G_copy = G_next



    ec = colour_edges(G_next)

    print(updated)
    print('no. cycle paths = ',ec.count('r'))
    if save == True:
        outfile = 'Graphmls\Graphpostupgrade' + '_' + str(L)+ '_' + str(Nt) + '_' + str(B)+ '_' + str(w)

        ox.io.save_graphml(G_next, filepath=outfile, gephi=False, encoding='utf-8')




    end = timer()

    print('update time = ',(end-start)/60)

    print(flowmat)

    return G_next, flowmat

def first_batch_edges():

    G,flowmat = upgrade_network(2000,100,3)

    nodelist = list(G.nodes)

    first_batch_edges = [(u,v,k,d) for u,v,k,d in G.edges(keys=True, data=True) if d['batch']==1]

    total_length = 0
    names = []
    flows = np.ones(len(first_batch_edges))
    i = 0

    for u,v,k,d in first_batch_edges:
        if 'name' in d:
            print(d['name'])
            names.append(d['name'])
        else:
            names.append('no name')

        flowindex = [nodelist.index(u),nodelist.index(v)]
        flows[i] = flowmat[flowindex[0],flowindex[1]]
        total_length = total_length + d['length']
        i = i+1

    print(total_length)
    columns = ['Street name','Cycle Flow']
    data = np.vstack((names,flows))
    df = pd.DataFrame(data,columns = columns)
    print(df.head())

def colour_by_batch():

    G_upgrade,flowmat = upgrade_network(160000,25,5)


    # nodes,edges = ox.graph_to_gdfs(G_upgrade, nodes=True, edges=True)
    # cmap = plt.cm.get_cmap('viridis')
    # norm=plt.Normalize(vmin=edges['batch'].min(), vmax=edges['batch'].max())
    # sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    #sm.set_array([])

    cmap = plt.cm.jet  # define the colormap
    # extract all colors from the .jet map
    cmaplist = [cmap(i) for i in range(cmap.N)]


    # create the new map
    cmap = mpl.colors.LinearSegmentedColormap.from_list('Custom cmap', cmaplist, cmap.N)

    ec = ox.plot.get_edge_colors_by_attr(G_upgrade,'batch',cmap=cmap)

    # define the bins and normalize
    bounds = np.linspace(0, 20, 21)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = ox.plot_graph(G_upgrade, node_size=0, edge_color=ec, edge_linewidth=0.5, edge_alpha=0.7,save=False, show=False, filepath = 'lpic_figs/coloured_by_batch.pdf',bgcolor='lightgray')
    cb = plb.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm,spacing='proportional', ticks=bounds, boundaries=bounds, format='%1i')
    plt.show()
    #fig.savefig('lpic_figs/coloured_by_batch.pdf')
