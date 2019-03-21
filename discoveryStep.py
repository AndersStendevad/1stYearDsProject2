import networkx as nx
import fileManagement as fm
import pandas as pd
import matplotlib.pyplot as plt
from networkx.algorithms import community
import numpy as np

def discoveryStep(freshStart=True):
    if not freshStart:
        return None
    dataframe = fm.backboningIntoMemory()


    fm.communityToCsv(dataframe)

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

#turn pandas dataframe to biadjency list
def nx_graph_from_biadjacency_pandas_df(df):
    B = nx.Graph()
    for i in df.index:
        B.add_node(i, bipartite=1)
        for j in df.columns:
            B.add_node(j, bipartite=0)
            if (df.ix[i,j] > 0):
                B.add_edge(i, j, weight=df.ix[i,j])
    return B

A = nx_graph_from_biadjacency_pandas_df(df)
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

def relevant_community(community, treshold):
    n_communities = 0
    relevant_list = []
    for i in community:
        if len(i) < treshold:
            continue
        else:
            n_communities += 1
            relevant_list.append(i)
            
    return relevant_list, n_communities

print(relevant_community(find_community(A), 5000))