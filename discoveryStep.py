import networkx as nx
import fileManagement as fm
import pandas as pd
import matplotlib.pyplot as plt
from networkx.algorithms import community
import numpy as np
from os import path

def discoveryStep(freshStart=True):
    if not freshStart:
        return None
    dataframe = fm.backboningIntoMemory()

    ##turn .csv to pandas dataframe
    with open('Data/communitydata.csv') as f:
    	pdcsv = pd.read_csv(f)
    	df = pd.DataFrame(pdcsv)

    df = pd.DataFrame(df)

    #turn pandas data frame to edgelist
    def nx_graph (df):
    	B = nx.Graph()
    	for i in df.index:
    		src_node = df["src"][i]
    		trg_node = df["trg"][i]
    		score = df['nij'][i]
    		B.add_edge(trg_node,src_node,weight=score)

    	return B

    B = nx_graph(df)
    C = nx.from_pandas_edgelist(df, source='src', target='trg', edge_attr='score') #same as B, but with networkx

    ###########COMMUNITIES#################
    def find_community(G):
    	which_community = input("Which community algorithm do you want to use: lpc, gmc, or klb? ")
    	if which_community == 'lpc':
    		#returns communities as sets of nodes
    		return list(nx.algorithms.community.label_propagation_communities(G))
    	elif which_community == 'gmc':
    		#returns communities as sets of nodes
    		return list(nx.algorithms.community.greedy_modularity_communities(G))
    	elif which_community == 'klb':
    		#returns a pair of sets of nodes representing the bipartition.
    		return list(nx.algorithms.community.kernighan_lin_bisection(G))

    treshold = int(input("What should minimum number of nodes in community be? "))

    n_communities = 0
    relevant_list = []
    for i in find_community(B):
    	if len(i) < treshold:
    		continue
    	else:
    		n_communities += 1
    		relevant_list.append(i)

    print(relevant_list, n_communities)


    fm.communityToCsv(dataframe)
