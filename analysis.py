import geopandas as gpd
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import osmnx as ox
import networkx as nx
from networkx.linalg.graphmatrix import adjacency_matrix
import matplotlib
import matplotlib.patches as mpatches
from commutedata import *
import sys

def init_graph(filepath):
    G = ox.io.load_graphml(filepath)
    Gp = ox.project_graph(G)
    nodes = Gp.nodes
    edges = G.edges
    Ag = adjacency_matrix(Gp, nodelist=None, weight='length')

    return [Gp, nodes, edges, Ag]


def random_shortest_path(G,ODoption = 'random',Gbbox = None):


    #print(nodes)
    ODpair = getOD(G,ODoption,Gbbox)

    if nx.has_path(G,ODpair[0],ODpair[1]):
        path = ox.shortest_path(G,ODpair[0],ODpair[1])

        pathedges = []
        for i in range(len(path)-1):
            pathedges.append([path[i],path[i+1]])

        #print(pathedges)

        ec = colour_edges(G)

        edgelist = list(G.edges)
        l = []
        for e in pathedges:
            index = edgelist.index((e[0],e[1],0))

            if ec[index] == 'r':
                ec[index] = 0
                ec[index] = 'b'
                l.append(1)
            if ec[index] == 'w':
                ec[index] = 0
                ec[index] = 'g'
                l.append(0)




        if len(l) == 0:
            pct_cycle = 0
        else:
            pct_cycle = (sum(l)/len(l))*100

        length = nx.shortest_path_length(G,ODpair[0],ODpair[1])




    else:
        path = [0]
        ec = colour_edges(G)
        pct_cycle = 0
        length = 0

    return path , ec, pct_cycle,length


def getOD(G,ODoption,Gbbox):
    if ODoption == 'random':
        nodes = G.nodes
        nodes = list(nodes)
        #print(nodes)
        ODpair = np.random.choice(nodes,2)

    if ODoption == 'centre':
        ODpair = commute_to_bbox(G,Gbbox)
        print(ODpair)

    if ODoption == 'lsoa':
        ids, centroids, normed_matrix = initialiselsoa()
        ODpair = lsoapair(G, ids, centroids, normed_matrix)

    else:
        print('invalid ODoption')
        ODpair = [-1,-1]

    return ODpair

def commute_to_bbox(G,Gbbox):
    allnodes = list(G.nodes)
    bboxnodes=list(Gbbox.nodes)
    origins  = [x for x in allnodes if x not in bboxnodes]
    destinations = bboxnodes

    ODpair = [np.random.choice(origins,1)[0],  np.random.choice(destinations,1)[0]]

    return ODpair



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

def adjust_weights(G,c):
    edge_index = []
    node_list = list(G.nodes)
    #identify index of non cycle lanes
    for u,v,k,d in G.edges(keys=True, data=True):
        bi = False
        if "bicycle" in d: #kind of uggly but not every edge has the bicycle tag
            if d['bicycle']=='designated':
                bi = True

        if d['highway']=='cycleway':
            pass


        elif 'cycleway' in d:
            pass
        elif bi:
            pass
        else:
            d['length'] = d['length'] * c



    return G



    #ec = ['r' if data['highway'] == 'cycleway' elif data['bicycle'] == 'designated' else 'w' for u, v, key, data in all[0].edges(keys=True, data=True)]
    #fig, ax = ox.plot_graph(all[0], node_size=0, edge_color=ec, edge_linewidth=1.5, edge_alpha=0.7)

def lsoapair(G,ids,centroids,m):
    originlsoa = np.random.choice(ids,1)
    indexorigin = ids.index(originlsoa)
    origincoords = centroids[indexorigin][::-1]
    flowprob = m[indexorigin]

    destinationlsoa = np.random.choice(ids,1,list(flowprob))
    indexdestination = ids.index(destinationlsoa)
    destinationcoords = centroids[indexdestination][::-1]

    nodeorigin = ox.get_nearest_node(G, origincoords, method='haversine', return_dist=False)
    nodedestination = ox.get_nearest_node(G, destinationcoords, method='haversine', return_dist=False)


    ODpair = [nodeorigin,nodedestination]

    return ODpair


if __name__ == '__main__':

    Gall = ox.io.load_graphml('Graphall')
    centre = ox.io.load_graphml('Graphbriscentre')





    ec = colour_edges(Gall)


    G_adj = adjust_weights(Gall,1)



    #for plotting highlighted graph
    #fig, ax = ox.plot_graph(all[0], node_size=0, edge_color=ec, edge_linewidth=1.5, edge_alpha=0.7,show = False)
    # ax.set_title('Graph of road network in Bristol with cycle paths highlighted', fontsize = 18)
    #
    #
    #
    # red_patch = mpatches.Patch(color='red', label='Roads with cycle paths')
    #
    # ax.legend(handles=[red_patch])

    #plt.show()


    #print(list(all[0].edges)[1])

    path, ecpath, pct_cycle,length = random_shortest_path(G_adj,ODoption = 'lsoa',Gbbox = centre)
    print(path)
    #fig, ax = ox.plot_graph(Gall, node_size=0, edge_color=ecpath, edge_linewidth=1.5, edge_alpha=0.7)
