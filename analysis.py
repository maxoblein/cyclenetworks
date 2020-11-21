import geopandas as gpd
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import osmnx as ox
import networkx as nx
from networkx.linalg.graphmatrix import adjacency_matrix


def init_graph(filepath):
    G = ox.io.load_graphml(filepath)
    Gp = ox.project_graph(G)
    nodes = Gp.nodes
    edges = G.edges
    Ag = adjacency_matrix(Gp, nodelist=None, weight='length')

    return [Gp, nodes, edges, Ag]


def random_shortest_path(G):

    nodes = G.nodes
    nodes = list(nodes)
    #print(nodes)
    ODpair = np.random.choice(nodes,2)
    path = ox.shortest_path(G,ODpair[0],ODpair[1])

    pathedges = []
    for i in range(len(path)-1):
        pathedges.append([path[i],path[i+1]])

    #print(pathedges)

    ec = colour_edges(G)

    edgelist = list(G.edges)
    for e in pathedges:
        index = edgelist.index((e[0],e[1],0))

        if ec[index] == 'r':
            ec[index] = 0
            ec[index] = 'b'
        if ec[index] == 'w':
            ec[index] = 0
            ec[index] = 'g'







    return path , ec


def find_missing_links():

    return 0

def colour_edges(G):
    ec = []
    for u,v,k,d in G.edges(keys=True, data=True):
        bi = False
        if "bicycle" in d: #kind of uggly but not every edge has the bicycle tag
            if d['bicycle']=='designated':
                bi = True

        if d['highway']=='cycleway':
            ec.append('r')


        elif 'cycleway' in d:
            ec.append('r')
        elif bi:
            ec.append('r')
        else:
            ec.append('w')


    return ec





    #ec = ['r' if data['highway'] == 'cycleway' elif data['bicycle'] == 'designated' else 'w' for u, v, key, data in all[0].edges(keys=True, data=True)]
    #fig, ax = ox.plot_graph(all[0], node_size=0, edge_color=ec, edge_linewidth=1.5, edge_alpha=0.7)



if __name__ == '__main__':
    cycle = init_graph('Cyclenetwork')
    all = init_graph('Graphall')





    ec = colour_edges(all[0])
    #fig, ax = ox.plot_graph(all[0], node_size=0, edge_color=ec, edge_linewidth=1.5, edge_alpha=0.7)
    #print(list(all[0].edges)[1])

    path, ecpath = random_shortest_path(all[0])
    #print(path)
    fig, ax = ox.plot_graph(all[0], node_size=0, edge_color=ecpath, edge_linewidth=1.5, edge_alpha=0.7)







'''
    for u,v,k in G.edges(keys=True, data=False):
        if (u==e[0] and v==e[1]):
            if ec[counter] == 'r':
                ec[counter] = 'g'
            if ec[counter] == 'w':
                ec[counter] = 'g'
'''
