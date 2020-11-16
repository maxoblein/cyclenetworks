import geopandas as gpd
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import osmnx as ox
from networkx.linalg.graphmatrix import adjacency_matrix

def init_graph(filepath):
    G = ox.io.load_graphml(filepath)
    Gp = ox.project_graph(G)
    nodes = Gp.nodes
    edges = G.edges
    Ag = adjacency_matrix(Gp, nodelist=None, weight='length')

    return [Gp, nodes, edges, Ag]


def random_shortest_path(G,Ag):
    size = Ag.shape[0]
    ODindex = np.random.choice(size, 2)
    print(ODindex)
    nodes =list(G.nodes)

    ODpair = [nodes[ODindex[0]],nodes[ODindex[1]]]
    path = ox.distance.shortest_path(G, ODpair[0], ODpair[1], weight='length')
    return path


def find_missing_links():

    return 0






if __name__ == '__main__':
    cycle = init_graph('Cyclenetwork')
    all = init_graph('Graphall')
