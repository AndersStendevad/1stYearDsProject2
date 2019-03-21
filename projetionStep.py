import networkx as nx
import libraries.network_map2 as nm2
import libraries.backboning as bb
import fileManagement as fm
import networkx as nx
from os import path


def projetionStep(projection_type="ycn", freshStart=True, on_nodes = 'b'):
    if not freshStart:
        return None
    filename = fm.rawData

    if on_nodes != 'b':
        out_filename = create_out_filename(projection_type,filename,on_nodes)
        if projection_exists(out_filename):
            print('Projection file aready exists!')
            fm.projetionFile = out_filename
            return
    else:
        print('The back boning is going to run on the last existing file!')
        out_filename = create_out_filename(projection_type,filename,'c')
        if projection_exists(out_filename):
            print('Customer projection file aready exists!')
            fm.projetionFile = out_filename
        out_filename = create_out_filename(projection_type,filename,'q')
        if projection_exists(out_filename):
            print('Query projection file aready exists!')
            fm.projetionFile = out_filename
            return
    path = fm.path(filename)
    G = nx.read_adjlist(path,delimiter = " ", nodetype = int)
    print('Started to read in the network')
    nodes = nx.algorithms.bipartite.sets(G)

    if on_nodes == 'b' or on_nodes == 'c':
        print('Customer projection '+projection_type+' started')
        customers = sorted(list(nodes[1]))
        C = projection(G,customers,projection_type)
        print('Started to save customer projection')
        if C == "Cannot run":
            return
        saveProjectoin(C,out_filename)
        fm.projetionFile = out_filename
    if on_nodes == 'b' or on_nodes == 'q':
        queries = sorted(list(nodes[0]))
        print('Queries projection '+projection_type+' started')
        Q = projection(G,queries,projection_type)#projected graph of queries
        if Q == "Cannot run":
            return
        print('Started to save query projection')
        saveProjectoin(Q,out_filename)
        fm.projetionFile = out_filename

def saveProjectoin(G,out_filename):
        df = transform_for_bb(G)
        fm.saveToCsv(df,out_filename)
def projection_exists(out_filename):
    return path.exists('Data/'+ out_filename)

def create_out_filename(projection_type,origin_filename,node_type):
    filename = origin_filename.split('.')[0]
    out_filename =  projection_type + '_' + filename + '_'+node_type+'.csv'
    return out_filename

def transform_for_bb(G):
    '''Transforms graph into a pandas DataFrame'''
    G_df = nx.to_pandas_edgelist(G)
    G_df.columns = ('src', 'trg', 'nij')
    print(G_df)
    G_df = bb.make_symmetric(G_df)
    return G_df

def simple(G,nodes):
    '''Does simple projection'''
    return nm2.simple(G,nodes)

def hyperbolic(G,nodes):
    '''Does hyperbolic projection'''
    try:
        return nm2.hyperbolic(G,nodes)
    except MemoryError:
        print("MemoryError with hyperbolic\n this is a known error. The program will continue if possible\n")
        return "Cannot run"

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
