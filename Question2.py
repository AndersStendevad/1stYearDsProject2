import networkx as nx
import fileManagement as fm
import pandas as pd
import matplotlib.pyplot as plt
from networkx.algorithms import community
import numpy as np

with open('noise_corrected_ydata-ysm-advertiser-phrase-adjlist_probs.csv') as f:
    pdcsv = pd.read_csv(f)
    df = pd.DataFrame(pdcsv)
    
df = pd.DataFrame(df)

def nx_graph(df):
    B = nx.Graph()
    for i in df.index:
        src_node = df["src"][i]
        trg_node = df["trg"][i]
        score = df['nij'][i]
        B.add_edge(trg_node,src_node,weight=score)
        
    return B

B = nx_graph(df)
D = nx.from_pandas_edgelist(df, source='src', target='trg', edge_attr='score', create_using=nx.DiGraph())

out_degree_two = []
for i in D:
    if D.out_degree(i) == 2:
        out_degree_two.append(i)

def readCommunity(filename):
    communities = fm.dataIntoMemory(filename).fillna(-1)
    list_with_NaN_communities = [communities.ix[:,x].tolist() for x in communities.columns.tolist()]
    list_communities = []
    for list in list_with_NaN_communities:
        list_communities.append([value for value in list if value != -1])
    return list_communities


kjkk= readCommunity('communityDataPropsNoiseCorrected.csv')

for i in kjkk[1:]:
    for customer in i:
        if int(customer) in out_degree_two:
            continue
        else:
            i.remove(customer)


def community_to_csv(rc):
    columns = []
    for i in range(len(rc)):
        columns.append('comunity'+ str(i))
        
    df2 = pd.DataFrame(rc)
    df2 = df2.transpose()
    df2.columns = columns

    return df2


b = community_to_csv(kjkk)

fm.saveToCsv(b,'kjkk.csv')

for i in range(1, len(kjkk)):
    print(B.edges(kjkk[i]))
