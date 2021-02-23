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
