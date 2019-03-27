import fileManagement as fm
import networkx as nx
import measures as me
import pandas as pd

def main():
    measures = me.Measures(fm.rawData)
    list_communities = measures.readCommunity("communityDataPropsNoiseCorrected.csv")
    list_query_shares = []
    counter = 0
    list_len_community = 0
    for community in list_communities:
        list_len_community +=len(community)
        counter +=1
        query_shares = measures.get_query_shares(community)
        list_nodes_over_50 = []
        for query in query_shares:
            if query[1] < 50:
                break
            list_nodes_over_50.append((query[0],len(community)))
        if len(list_nodes_over_50) != 0:
            list_query_shares.append(list_nodes_over_50)
    print(list_query_shares)
    print(list_len_community/counter)
    #[[(73942, 126)], [(312778, 63), (309127, 63)], [(448275, 63)], [(331075, 61)], [(217984, 68)], [(85191, 66)], [(32248, 75)], [(377534, 90), (373967, 90)], [(46244, 77)]]

def question_three(community_list):
    pass

def readCommunity(filename):
    communities = fm.dataIntoMemory(filename).fillna(-1)
    list_with_NaN_communities = [communities.ix[:,x].tolist() for x in communities.columns.tolist()]
    list_communities = []
    for list in list_with_NaN_communities:
        list_communities.append([value for value in list if value != -1])
    return list_communities[1:]

def read_raw_data():
    queries = set()
    customer_queries = {}

    with open('Data/'+fm.rawData) as rawF:

        lines = rawF.readlines()
        customer = None
        for line in lines:
            #if customer in queries:
            #    break
            line = line.split()
            customer = line[0]
            customer_queries[customer] = set(line[1:])
            queries.update(set(line[1:]))
    return queries,customer_queries

def something():
    list_files = ["communityDataPropsMaximumSpanningTree.csv","communityDataPropsNaive.csv","communityDataPropsNoiseCorrected.csv","communityDataSimpleMaximumSpanningTree.csv","communityDataSimpleNaive.csv","communityDataSimpleNoiseCorrected.csv"]
    for file in list_files:
        list_communities = readCommunity(file)
        counter = 0
        for community in list_communities:
            if len(community) > 60:
                counter += 1
        print(counter,"communities over 60",file)
        G = nx.read_adjlist(fm.path(fm.rawData),delimiter = " ", nodetype = int)
        print('Started to read in the network')
        nodes = nx.algorithms.bipartite.sets(G)
        customers = sorted(list(nodes[1]))
        queries = sorted(list(nodes[0]))



if __name__ == '__main__':
    main()
