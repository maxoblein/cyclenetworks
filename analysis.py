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


def random_shortest_path(G,ODoption = 'random',Gbbox = None,ids = 0,centroids = 0,normed_matrix = 0,G_true = 0):
    #Find a shortest path using a prescribed demaand model.


    ODpair = getOD(G,ODoption,Gbbox, ids=ids, centroids=centroids, normed_matrix=normed_matrix)

    if nx.has_path(G,ODpair[0],ODpair[1]):
        path = ox.shortest_path(G,ODpair[0],ODpair[1])

        pathedges = []
        for i in range(len(path)-1):
            pathedges.append([path[i],path[i+1]])

        #print(pathedges)

        ec = colour_edges(G)

        edgelist = list(G_true.edges)
        l_cycle = []
        l_all = []
        for e in pathedges:
            index = edgelist.index((e[0],e[1],0))
            edgelength = G_true.edges[(e[0],e[1],0)]['length']


            if ec[index] == 'r':
                ec[index] = 0
                ec[index] = 'b'
                l_cycle.append(edgelength)
                l_all.append(edgelength)
            if ec[index] == 'w':
                ec[index] = 0
                ec[index] = 'g'
                l_all.append(edgelength)




        if len(l_all) == 0:
            pct_cycle = 0
        else:

            pct_cycle = (sum(l_cycle)/sum(l_all))*100

        length = nx.shortest_path_length(G,ODpair[0],ODpair[1])




    else:
        path = [0]
        ec = colour_edges(G)
        pct_cycle = 0
        length = 0

    return path , ec, pct_cycle,length


def getOD(G,ODoption,Gbbox,ids = 0,centroids = 0,normed_matrix = 0):
    print(ODoption)
    # gets the od pair of the prescribed demand model
    if ODoption == 'random':
        nodes = G.nodes
        nodes = list(nodes)
        #print(nodes)
        ODpair = np.random.choice(nodes,2)
        return ODpair
    if ODoption == 'centre':
        ODpair = commute_to_bbox(G,Gbbox)
        print(ODpair)
        return ODpair
    if ODoption == 'lsoa':
        ODpair = lsoapair(G, ids, centroids, normed_matrix)
        return ODpair
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

def plot_lsoa():
    G = ox.io.load_graphml('Graphmls/Graphall')
    ids, centroids, normed_matrix = initialiselsoa()
    X = [coord[0] for coord in centroids]
    Y = [coord[1] for coord in centroids]
    X_ar = np.array(X)
    Y_ar = np.array(Y)



    centroid_nodes = ox.distance.get_nearest_nodes(G,X_ar,Y_ar,method = 'balltree')

    nc = ['r' if node in centroid_nodes else 'w' for node in G.nodes()]
    ns = [40 if node in centroid_nodes else 5 for node in G.nodes()]

    fig, ax = ox.plot_graph(G,node_size = ns, node_color = nc)


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
    G_copy = G.copy()
    edge_index = []
    node_list = list(G_copy.nodes)
    cycmat = np.zeros((len(node_list),len(node_list)))
    #identify index of non cycle lanes
    for u,v,k,d in G_copy.edges(keys=True, data=True):
        bi = False
        if "bicycle" in d: #kind of uggly but not every edge has the bicycle tag
            if d['bicycle']=='designated':
                bi = True

        if d['highway']=='cycleway':
            cycmat[node_list.index(u)][node_list.index(v)] = 1


        elif 'cycleway' in d:
            cycmat[node_list.index(u)][node_list.index(v)] = 1
        elif bi:
            cycmat[node_list.index(u)][node_list.index(v)] = 1
        else:
            d['length'] = d['length'] * c



    return G_copy, cycmat

def find_total_cycle_length(G):
    length = 0
    for u,v,k,d in G.edges(keys=True, data=True):
        bi = False
        if "bicycle" in d: #kind of uggly but not every edge has the bicycle tag
            if d['bicycle']=='designated':
                bi = True

        if d['highway']=='cycleway':
            length = length + d['length']


        elif 'cycleway' in d:
            length = length + d['length']
        elif bi:
            length = length + d['length']
        else:
            pass

    return length

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
