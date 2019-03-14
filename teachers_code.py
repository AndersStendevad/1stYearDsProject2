import networkx as nx
import backboning as bb
import network_map2 as nm2
import matplotlib.pyplot as plt

def plot_network(G, factor, weight="weight"):
    linewidth = [d[weight] * factor for (u, v, d) in G.edges(data = True)]
    nx.draw_kamada_kawai(G, width = linewidth, labels = {n: n for n in G.nodes})
    plt.show()

def transform_for_bb(G):
    G_df = nx.to_pandas_edgelist(G)
    G_df.columns = ('src', 'trg', 'nij')
    G_df = bb.make_symmetric(G_df)
    return G_df

G = nx.read_adjlist("toy_data.txt", delimiter = " ", nodetype = int)

nodes = nx.algorithms.bipartite.basic.sets(G)
rows = sorted(list(nodes[1]))
cols = sorted(list(nodes[0]))
nx.draw_kamada_kawai(G, labels = {n: n for n in G.nodes}, node_color = ['b' if n in cols else 'r' for n in G.nodes])
plt.show()

G_simple = nm2.simple(G, rows)
plot_network(G_simple, 2)

G_hyperbolic = nm2.hyperbolic(G, rows)
plot_network(G_hyperbolic, 20)

G_ycn = nm2.ycn(G, rows)
plot_network(G_ycn, 80)

G_probs = nm2.probs(G, rows)
plot_network(G_probs, 10)

G_simple_df = transform_for_bb(G_simple)
G_simple_df_naive = bb.naive(G_simple_df, undirected = True)
print(bb.test_densities(G_simple_df_naive, 0, 3, 1))
G_simple_df_naive_bb = bb.thresholding(G_simple_df_naive, 1)
G_simple_naive = nx.from_pandas_edgelist(G_simple_df_naive_bb, source = 'src', target = "trg", edge_attr = ('nij', 'score'))
plot_network(G_simple_naive, 2, weight = "nij")

G_simple_df_nc = bb.noise_corrected(G_simple_df, undirected = True)
print(G_simple_df_nc)
print(bb.test_densities(G_simple_df_nc, 0, 1, .1))
G_simple_df_nc_bb = bb.thresholding(G_simple_df_nc, 0.6)
G_simple_nc = nx.from_pandas_edgelist(G_simple_df_naive_bb, source = 'src', target = "trg", edge_attr = ('nij', 'score'))
plot_network(G_simple_naive, 2, weight = "nij")

comms = list(nx.algorithms.community.label_propagation.label_propagation_communities(G_simple_nc))
nx.draw_kamada_kawai(G_simple_nc, labels = {n:n for n in G_simple_nc.nodes}, node_color = ['b' if n in comms[0] else 'r' for n in G_simple_nc.nodes])
plt.show()

G_simple_nc_conncomps = list(nx.connected_components(G_simple_nc))
print(G_simple_nc_conncomps)
