from analysis import *
from commutedata import *
#ox.utils.config(use_cache=True, log_console=True)

network_pre = ox.io.load_graphml('Graphall')
network_post = ox.io.load_graphml('Graphpostupgrade_500_20_100')
#centrenet = ox.io.load_graphml('Graphbriscentre')

def compare_pct(G1,G2,filepath):
    network_pre = G1
    network_post = G2
    ids, centroids, normed_matrix = initialiselsoa()
    G_adj_pre,cycmat = adjust_weights(network_pre,25)
    G_adj_post, cycmat = adjust_weights(network_post,25)



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


    plt.savefig(filepath)







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
