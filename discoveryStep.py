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
    df = fm.backboningIntoMemory()
    B = nx_graph(df)
    C = nx.from_pandas_edgelist(df, source='src', target='trg', edge_attr='score') #same as B, but with networkx
    treshold1 = int(input("What should minimum number of nodes in community be? "))

    rc = relevant_community(find_community(B), treshold1)

    fm.communityToCsv(community_to_csv(rc))


#turn pandas data frame to edgelist
def nx_graph (df):
	B = nx.Graph()
	for i in df.index:
		src_node = df["src"][i]
		trg_node = df["trg"][i]
		score = df['nij'][i]
		B.add_edge(trg_node,src_node,weight=score)

	return B


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
    count = 0
    relevant_list = []
    for i in community:
        if len(i) < treshold:
            continue
        else:
            count += 1
            relevant_list.append(i)
            
    return relevant_list

#turns the relevant communities into .csv file
def community_to_csv(rc):
    columns = []
    for i in range(len(rc)):
        columns.append('comunity'+ str(i))
        
    df2 = pd.DataFrame(rc)
    df2 = df2.transpose()
    df2.columns = columns

    return df2
