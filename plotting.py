#script to plot graphs from graphml file for report

from upgrade import *
import sys
from distributions import *

if __name__ == '__main__':

    if sys.argv[1] == 'plt_net':
        infile = sys.argv[2]
        outfile = sys.argv[3]


        G = ox.io.load_graphml(infile)
        ec = colour_edges(G)



        plot_lpic(G,ec,save = True,show = False,filepath = outfile)



    if sys.argv[1] == 'cmp':
        G1 = ox.io.load_graphml(sys.argv[2])
        G2 = ox.io.load_graphml(sys.argv[3])
        filepath = sys.argv[4]

        compare_pct(G1,G2,filepath)

    # else:
    #     network_1 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_0')
    #     network_2 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_1')
    #     network_3 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_2')
    #     network_4 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_3')
    #     network_5 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_4')
    #     network_6 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_5')
    #     network_7 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_6')
    #     network_8 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_7')
    #     network_9 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_8')
    #     network_10 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_9')
    #     network_11 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_10')
    #     network_12 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_11')
    #     network_13 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_12')
    #     network_14 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_13')
    #     network_15 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_14')
    #     network_16 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_15')
    #     network_17 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_16')
    #     network_18 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_17')
    #     network_19 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_18')
    #     network_20 = ox.io.load_graphml('Graphmls/batches_2000_1000_20/batch_19')
    #     ids, centroids, normed_matrix = initialiselsoa()
    #     G_adj_1,cycmat = adjust_weights(network_1,25)
    #     G_adj_2,cycmat = adjust_weights(network_2,25)
    #     G_adj_3,cycmat = adjust_weights(network_3,25)
    #     G_adj_4,cycmat = adjust_weights(network_4,25)
    #     G_adj_5,cycmat = adjust_weights(network_5,25)
    #     G_adj_6,cycmat = adjust_weights(network_6,25)
    #     G_adj_7,cycmat = adjust_weights(network_7,25)
    #     G_adj_8,cycmat = adjust_weights(network_8,25)
    #     G_adj_9,cycmat = adjust_weights(network_9,25)
    #     G_adj_10,cycmat = adjust_weights(network_10,25)
    #     G_adj_11,cycmat = adjust_weights(network_11,25)
    #     G_adj_12,cycmat = adjust_weights(network_12,25)
    #     G_adj_13,cycmat = adjust_weights(network_13,25)
    #     G_adj_14,cycmat = adjust_weights(network_14,25)
    #     G_adj_15,cycmat = adjust_weights(network_15,25)
    #     G_adj_16,cycmat = adjust_weights(network_16,25)
    #     G_adj_17,cycmat = adjust_weights(network_17,25)
    #     G_adj_18,cycmat = adjust_weights(network_18,25)
    #     G_adj_19,cycmat = adjust_weights(network_19,25)
    #     G_adj_20,cycmat = adjust_weights(network_20,25)
    #
    #
    #
    #
    #     d_1 = []
    #     d_2 = []
    #     d_3 = []
    #     d_4 = []
    #     d_5 = []
    #     d_6 = []
    #     d_7 = []
    #     d_8 = []
    #     d_9 = []
    #     d_10 = []
    #     d_11 = []
    #     d_12 = []
    #     d_13 = []
    #     d_14 = []
    #     d_15 = []
    #     d_16 = []
    #     d_17 = []
    #     d_18 = []
    #     d_19 = []
    #     d_20 = []
    #
    #
    #
    #     for i in range(500):
    #         print(i)
    #         path_1, ecpath_1, pct_cycle_1, length_1 = random_shortest_path(G_adj_1,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_1)
    #         path_2, ecpath_2, pct_cycle_2, length_2 = random_shortest_path(G_adj_2,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_2)
    #         path_3, ecpath_3, pct_cycle_3, length_3 = random_shortest_path(G_adj_3,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_3)
    #         path_4, ecpath_4, pct_cycle_4, length_4 = random_shortest_path(G_adj_4,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_4)
    #         path_5, ecpath_5, pct_cycle_5, length_5 = random_shortest_path(G_adj_5,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_5)
    #         path_6, ecpath_6, pct_cycle_6, length_6 = random_shortest_path(G_adj_6,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_6)
    #         path_7, ecpath_7, pct_cycle_7, length_7 = random_shortest_path(G_adj_7,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_7)
    #         path_8, ecpath_8, pct_cycle_8, length_8 = random_shortest_path(G_adj_8,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_8)
    #         path_9, ecpath_9, pct_cycle_9, length_9 = random_shortest_path(G_adj_9,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_9)
    #         path_10, ecpath_10, pct_cycle_10, length_10 = random_shortest_path(G_adj_10,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_10)
    #         path_11, ecpath_11, pct_cycle_11, length_11 = random_shortest_path(G_adj_11,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_11)
    #         path_12, ecpath_12, pct_cycle_12, length_12 = random_shortest_path(G_adj_12,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_12)
    #         path_13, ecpath_13, pct_cycle_13, length_13 = random_shortest_path(G_adj_13,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_13)
    #         path_14, ecpath_14, pct_cycle_14, length_14 = random_shortest_path(G_adj_14,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_14)
    #         path_15, ecpath_15, pct_cycle_15, length_15 = random_shortest_path(G_adj_15,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_15)
    #         path_16, ecpath_16, pct_cycle_16, length_16 = random_shortest_path(G_adj_16,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_16)
    #         path_17, ecpath_17, pct_cycle_17, length_17 = random_shortest_path(G_adj_17,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_17)
    #         path_18, ecpath_18, pct_cycle_18, length_18 = random_shortest_path(G_adj_18,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_18)
    #         path_19, ecpath_19, pct_cycle_19, length_19 = random_shortest_path(G_adj_19,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_19)
    #         path_20, ecpath_20, pct_cycle_20, length_20 = random_shortest_path(G_adj_20,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_20)
    #
    #
    #         if len(path_1) > 50:
    #             d_1.append(pct_cycle_1)
    #
    #         if len(path_2) > 50:
    #             d_2.append(pct_cycle_2)
    #
    #         if len(path_3) > 50:
    #             d_3.append(pct_cycle_3)
    #
    #         if len(path_4) > 50:
    #             d_4.append(pct_cycle_4)
    #
    #         if len(path_5) > 50:
    #             d_5.append(pct_cycle_5)
    #
    #         if len(path_6) > 50:
    #             d_6.append(pct_cycle_6)
    #
    #         if len(path_7) > 50:
    #             d_7.append(pct_cycle_7)
    #
    #         if len(path_8) > 50:
    #             d_8.append(pct_cycle_8)
    #
    #         if len(path_9) > 50:
    #             d_9.append(pct_cycle_9)
    #
    #         if len(path_10) > 50:
    #             d_10.append(pct_cycle_10)
    #
    #         if len(path_11) > 50:
    #             d_11.append(pct_cycle_11)
    #
    #         if len(path_12) > 50:
    #             d_12.append(pct_cycle_12)
    #
    #         if len(path_13) > 50:
    #             d_13.append(pct_cycle_13)
    #
    #         if len(path_14) > 50:
    #             d_14.append(pct_cycle_14)
    #
    #         if len(path_15) > 50:
    #             d_15.append(pct_cycle_15)
    #
    #         if len(path_16) > 50:
    #             d_16.append(pct_cycle_16)
    #
    #         if len(path_17) > 50:
    #             d_17.append(pct_cycle_17)
    #
    #         if len(path_18) > 50:
    #             d_18.append(pct_cycle_18)
    #
    #         if len(path_19) > 50:
    #             d_19.append(pct_cycle_19)
    #
    #         if len(path_20) > 50:
    #             d_20.append(pct_cycle_20)
    #
    #
    #     data = [d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_8, d_9, d_10, d_11, d_12, d_13, d_14, d_15, d_16, d_17, d_18, d_19, d_20]
    #     fig, ax = plt.subplots()
    #     ax.boxplot(data)
    #     ind = np.arange(21)
    #     ax.set_xticks(ind)
    #     labels = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    #     ax.set_xticklabels(labels)
    #
    #
    #     plt.savefig('lpic_figs/cmp_2000_through_batches.pdf')
