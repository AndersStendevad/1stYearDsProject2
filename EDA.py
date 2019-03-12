import networkx as nx
import backboning as bb
import network_map2 as nm2
import matplotlib.pyplot as plt
import pandas as pd

filename = "ydata-ysm-advertiser-phrase-adjlist.txt"

def main():
    print("im not dead yet")
    G = nx.read_adjlist(path(filename),delimiter = " ", nodetype = int)
    print("im not dead yet")
    G = sample(G,100)
    print("im not dead yet")
    draw_ugly(G)

def sample(G,sampleSize):
    import random
    sampled_edges = random.sample(G.edges, sampleSize)
    X = nx.Graph()
    return X.add_edges_from(sampled_edges)

def draw_ugly(G):
    nx.draw(G)
    plt.show()


def draw_nicely(G):
    nodes = nx.algorithms.bipartite.sets(G)
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

main()
