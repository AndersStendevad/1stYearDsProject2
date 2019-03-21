import networkx as nx
import fileManagement as fm

def visualizationsStep():
    path = fm.path(fm.rawData)
    G = nx.read_adjlist(path, delimiter = " ", nodetype = int)

    G_nodes = nx.algorithms.bipartite.sets(G)

    # Basic figures
    print("------ totals ------")
    print("Customers: ", len(G_nodes[0]))
    print("Queries: ", len(G_nodes[1]))
    print()

    # Frequency of degrees
    degree_dict = {}
    for node in G_nodes[0]:
        degree_dict[G.degree(node)] = degree_dict.get(G.degree(node), 0) + 1

    key_s = ""
    counts_s = ""
    for key in sorted(degree_dict):
        key_s += str(key) + ", "
        counts_s += str(degree_dict[key]) + ", "

    print(key_s)
    print()
    print()
    print(counts_s)
