from analysis import *
from commutedata import *
#ox.utils.config(use_cache=True, log_console=True)

network_pre = ox.io.load_graphml('Graphmls\Graphall')
network_post = ox.io.load_graphml('Graphmls\Graphpostupgrade_500_20_100')
#centrenet = ox.io.load_graphml('Graphbriscentre')

def compare_pct(G1,G2,filepath):
    network_pre = G1
    network_post = G2
    ids, centroids, normed_matrix = initialiselsoa()
    G_adj_pre,cycmat = adjust_weights(network_pre,2)
    G_adj_post, cycmat = adjust_weights(network_post,2)



    d_pre = []
    d_post = []
    for i in range(500):
        print(i)
        path_pre, ecpath_pre, pct_cycle_pre, length_pre = random_shortest_path(G_adj_pre,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_pre)
        path_post, ecpath_post, pct_cycle_post, length_post = random_shortest_path(G_adj_post,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_post)

        if len(path_pre) > 50:
            d_pre.append(pct_cycle_pre)

        if len(path_post) > 50:
            d_post.append(pct_cycle_post)


    data = [d_pre, d_post]
    fig, ax = plt.subplots()



    ax.boxplot(data)

    ind = np.arange(3)
    ax.set_xticks(ind)
    labels = [' ','oneshot', 'single-edge']
    ax.set_xticklabels(labels)

    print('mean pre = ',np.mean(data[0]))
    print('mean post = ',np.mean(data[1]))
    plt.savefig(filepath)


def get_pcts(filepath,N,wt=2,return_lengths = False, plot = False, ODoption = 'lsoa'):
    network_pre = ox.io.load_graphml(filepath)
    ids, centroids, normed_matrix = initialiselsoa()
    G_adj_pre,cycmat = adjust_weights(network_pre,wt)
    d_pre = []
    lengths = []

    for i in range(N):
        print(i)
        path_pre, ecpath_pre, pct_cycle_pre, length_pre = random_shortest_path(G_adj_pre, ODoption = ODoption, ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_pre)
        edge_lens = []
        for j in range(len(path_pre)-1):
            edge = [path_pre[j],path_pre[j+1]]
            length = network_pre.edges[(edge[0],edge[1],0)]['length']
            edge_lens.append(length)
        path_len = sum(edge_lens)

        #collect data
        if len(path_pre) > 50:
            d_pre.append(pct_cycle_pre)
            lengths.append(path_len)

    if return_lengths == True:
        return d_pre,lengths

    if plot == True:
        plt.hist(d_pre,bins=25)
        plt.show()


    return d_pre









# fig1 = plt.figure()
# ax1 = fig1.add_subplot(111)
#
# ax1.hist(d,bins=25)
#
#
# #plt.savefig('lpic_figs/hist_lsoa_post_500_20_100.pdf')
#
# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111)
#
# ax2.hist(l,bins=25)
# ax2.set_title('Number of edges in shortest paths between OD pairs',fontsize=18)
# ax2.set_xlabel('Length',fontsize=16)
# ax2.set_ylabel('Frequency',fontsize=16)
# plt.show()
