import fileManagement as fm
import networkx as nx


def main():
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
        
def question_three(community_list):
    pass



def readCommunity(filename):
    communities = fm.dataIntoMemory(filename).fillna(-1)
    list_with_NaN_communities = communities.values.tolist()
    list_communities = []
    for list in list_with_NaN_communities:
        list_communities.append([value for value in list if value != -1])
    return list_communities

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

if __name__ == '__main__':
    main()
