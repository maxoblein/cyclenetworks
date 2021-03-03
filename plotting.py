#script to plot graphs from graphml file for report

from edgeflows import *
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

    else:
        network_1 = ox.io.load_graphml('Graphpostupgrade_2000_2_100-')
        network_2 = ox.io.load_graphml('Graphpostupgrade_2000_4_500-')
        network_3 = ox.io.load_graphml('Graphpostupgrade_2000_8_250')
        network_4 = ox.io.load_graphml('Graphpostupgrade_2000_10_200')
        network_5 = ox.io.load_graphml('Graphpostupgrade_2000_20_100')
        network_6 = ox.io.load_graphml('Graphpostupgrade_2000_40_50')
        ids, centroids, normed_matrix = initialiselsoa()
        G_adj_1,cycmat = adjust_weights(network_1,25)
        G_adj_2,cycmat = adjust_weights(network_2,25)
        G_adj_3,cycmat = adjust_weights(network_3,25)
        G_adj_4,cycmat = adjust_weights(network_4,25)
        G_adj_5,cycmat = adjust_weights(network_5,25)
        G_adj_6,cycmat = adjust_weights(network_6,25)




        d_1 = []
        d_2 = []
        d_3 = []
        d_4 = []
        d_5 = []
        d_6 = []


        for i in range(500):
            print(i)
            path_1, ecpath_1, pct_cycle_1, length_1 = random_shortest_path(G_adj_1,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_1)
            path_2, ecpath_2, pct_cycle_2, length_2 = random_shortest_path(G_adj_2,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_2)
            path_3, ecpath_3, pct_cycle_3, length_3 = random_shortest_path(G_adj_3,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_3)
            path_4, ecpath_4, pct_cycle_4, length_4 = random_shortest_path(G_adj_4,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_4)
            path_5, ecpath_5, pct_cycle_5, length_5 = random_shortest_path(G_adj_5,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_5)
            path_6, ecpath_6, pct_cycle_6, length_6 = random_shortest_path(G_adj_6,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_6)


            if len(path_1) > 50:
                d_1.append(pct_cycle_1)

            if len(path_2) > 50:
                d_2.append(pct_cycle_2)

            if len(path_3) > 50:
                d_3.append(pct_cycle_3)

            if len(path_4) > 50:
                d_4.append(pct_cycle_4)

            if len(path_5) > 50:
                d_5.append(pct_cycle_5)

            if len(path_6) > 50:
                d_6.append(pct_cycle_6)


        data = [d_1, d_2, d_3, d_4, d_5, d_6]
        fig, ax = plt.subplots()
        ax.boxplot(data)
        ind = np.arange(7)
        ax.set_xticks(ind)
        labels = ['', '2', '4', '8', '10', '20', '40']
        ax.set_xticklabels(labels)


        plt.savefig('lpic_figs/cmp_2000_var_batchsize.pdf')
