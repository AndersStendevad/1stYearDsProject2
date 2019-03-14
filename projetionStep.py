import libraries.network_map2 as nm2
import fileManagement as fm


def projetionStep(filename,projection_type):

    def path(filename):
        return "Data/"+filename

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
            '\'ycn\' for raandom walks based projection\n'+)

    G = nx.read_adjlist(path(filename),delimiter = " ", nodetype = int)
    nodes = nx.algorithms.bipartite.sets(G)
    fm.projectionToCsv(transform_for_bb(projection(G,nodes,projection_type)))
