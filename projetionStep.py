import networkx as nx
import libraries.network_map2 as nm2
import libraries.backboning as bb
import fileManagement as fm
import networkx as nx


def projetionStep(projection_type="ycn", freshStart=True, on_nodes = 'b'):
    if not freshStart:
        return None
    filename = fm.rawData
    path = fm.path(filename)
    G = nx.read_adjlist(path,delimiter = " ", nodetype = int)
    print('Started to read in the network')
    nodes = nx.algorithms.bipartite.sets(G)

    if on_nodes == 'b' or on_nodes == 'c':
        print('Customer projection '+projection_type+' started')
        customers = sorted(list(nodes[1]))
        C = projection(G,customers,projection_type)
        print('Started to save customer projection')
        saveProjectoin(C,projection_type,filename,'customer')
    if on_nodes == 'b' or on_nodes == 'q':
        queries = sorted(list(nodes[0]))
        print('Queries projection '+projection_type+' started')
        Q = projection(G,queries,projection_type)#projected graph of queries
        print('Started to save query projection')
        saveProjectoin(Q,projection_type,filename,'query')

def saveProjectoin(G,projection_type,origin_filename,node_type):
        df = transform_for_bb(G)

        filename = origin_filename.split('.')[0]
        fm.saveToCsv(df,projection_type + '_' + filename + '_'+node_type+'.csv')

def transform_for_bb(G):
    '''Transforms graph into a pandas DataFrame'''
    G_df = nx.to_pandas_edgelist(G)
    G_df.columns = ('src', 'trg', 'nij')
    G_df = bb.make_symmetric(G_df)
    return G_df

def simple(G,nodes):
    '''Does simple projection'''
    return nm2.simple(G,nodes)

def hyperbolic(G,nodes):
    '''Does hyperbolic projection'''
    return nm2.hyperbolic(G,nodes)

def resource_allocation(G,nodes):
    '''Does resource allocation projection'''
    return nm2.probs(G,nodes)

def random_walks(G,nodes):
    '''Projects according to random walks'''
    return nm2.ycn(G,nodes)

def projection(G,nodes,projection_type):
    '''Returns the type of projection'''

    if projection_type == "simple":
        return simple(G,nodes)
    elif projection_type == "hyperbolic":
        return hyperbolic(G,nodes)
    elif projection_type == "probs":
        return resource_allocation(G,nodes)
    elif projection_type == "ycn":
        return random_walks(G,nodes)
    else:
        print("There is no projection type: " + projection_type )
        print('The projection types are:\n '+
        '\'simple\' for simple projection\n'+
        '\'hyperbolic\' for hyperbolic projection\n'+
        '\'probs\' for  resource allocation projection\n'+
        '\'ycn\' for raandom walks based projection\n')
