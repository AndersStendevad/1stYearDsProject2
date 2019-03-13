import networkx as nx
import numpy as np
import backboning as bb
import network_map2 as nm2
import matplotlib.pyplot as plt
import pandas as pd
import random as rd

#filename = "ydata-ysm-advertiser-phrase-adjlist.txt"
filename = "toy_data.txt"

#####################################

def main():
    G = nx.read_adjlist(path(filename),
    delimiter = " ", nodetype = int)

    nodes = nx.algorithms.bipartite.sets(G)
    rows = sorted(list(nodes[1]))
    cols = sorted(list(nodes[0]))
    X = nm2.simple(G, rows) # I use X so G will be the same for all
    draw_nicely(X,nodes)
    #DataFrame = nx.to_pandas_dataframe(G, nodelist=rows)
    print(DataFrame)

#####################################

def sample(G,sampleSize):
    import random
    sampled_edges = random.sample(G.edges, sampleSize)
    X = nx.Graph()
    return X.add_edges_from(sampled_edges)

def draw_ugly(G):
    nx.draw_kamada_kawai(G)
    plt.show()


def draw_nicely(G,nodes):
    rows = sorted(list(nodes[1]))
    cols = sorted(list(nodes[0]))
    nx.draw_kamada_kawai(G, labels = {
    n:n for n in G.nodes
    },
    node_color =[ 'b' if n in cols else 'r' for n in G.nodes],
    node_size = 800,
    font_color = 'w'
    ) # Draw it
    plt.show() # show

def path(filename):
    return "Data/"+filename

#####################################

def allAlg(G,nodes):
    rows = sorted(list(nodes[1]))
    listOptions = ["simple","hyperbolic","jaccard","euclidean","cosine","pearson","probs"]
    alg = listOptions[rd.randint(0, len(listOptions))]

    if True:
        print(listOptions[0])
        X = nm2.simple(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

    if True:
        print(listOptions[1])
        X = nm2.hyperbolic(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

    if True:
        print(listOptions[2])
        X = nm2.jaccard(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

    if True:
        print(listOptions[3])
        X = nm2.euclidean(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

    if True:
        print(listOptions[4])
        X = nm2.cosine(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

    if True:
        print(listOptions[5])
        X = nm2.pearson(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

    if True:
        print(listOptions[6])
        X = nm2.probs(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

def randomAlg(G,nodes):
    rows = sorted(list(nodes[1]))
    listOptions = ["simple","hyperbolic","jaccard","euclidean","cosine","pearson","probs"]
    alg = listOptions[rd.randint(0, len(listOptions))]

    if alg == listOptions[0]:
        print(listOptions[0])
        X = nm2.simple(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

    if alg == listOptions[1]:
        print(listOptions[1])
        X = nm2.hyperbolic(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

    if alg == listOptions[2]:
        print(listOptions[2])
        X = nm2.jaccard(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

    if alg == listOptions[3]:
        print(listOptions[3])
        X = nm2.euclidean(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

    if alg == listOptions[4]:
        print(listOptions[4])
        X = nm2.cosine(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

    if alg == listOptions[5]:
        print(listOptions[5])
        X = nm2.pearson(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

    if alg == listOptions[6]:
        print(listOptions[6])
        X = nm2.probs(G, rows) # I use X so G will be the same for all
        draw_nicely(X,nodes)

#####################################

if __name__ == '__main__':
    main()
