import fileManagement as fm
import networkx as nx
import pandas as pd

class Measures:
    G = None

    def __init__(self, adj_list_filename,  graph=None):
        print("Loading graph: ", adj_list_filename)
        if graph != None:
            G = graph
        else:
            self.G = nx.read_adjlist(fm.path(adj_list_filename),delimiter = " ", nodetype = int)
            G_set = nx.bipartite.maximum_matching(self.G)

    # Returns a list of all quesries a customer (or list of customers) has bid on.
    # Queries repeat - use set() to get a list of unique queries.
    def get_queries(self, customers):
        return [v for x,v in list(self.G.edges(customers))]

    # Returns a sorted list (of tuples) of counts of all queries assiciated with a list 
    # of customers (that is, a community)
    #
    # Format: (query, count) ///  e.g. (54555, 27)
    def get_query_counts(self, customers):
        query_dict = {}
    
        for query in self.get_queries(customers):
            query_dict[query] = query_dict.get(query, 0) + 1

        return sorted(query_dict.items(), key=lambda x: x[1])[::-1]

    # Returns a sorted list (of tuples) of all queries and the share of customers who bit on 
    # that query in a given community.
    #
    # Format: (query, share%) /// e.g. (54555, 0.27)
    def get_query_shares(self, customers):
        return [(x[0],(x[1]/len(customers)*100)) for x in get_query_counts(customers)]

    # -------- helpers --------

    # Returns the value of a tuple
    def get_value(self, tup, idx=1):
        return [x[idx] for x in tup][0]
