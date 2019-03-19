import libraries.backboning as bb
import networkx as nx
import fileManagement as fm

def backboningStep(freshStart=True):
    if freshStart == False:
        return None

    dataframe = fm.projetionIntoMemory()
    print(dataframe)

    bb_df = bb.noise_corrected(dataframe)
    print(bb_df)

    # G_simple_test = nx.from_pandas_edgelist(G_simple_df_naive_bb, source = 'src', target = "trg", edge_attr = ('nij', 'score'))
    # plot_network(G_simple_test, 2, weight = "nij")

    fm.backboningToCsv(dataframe)

# def transform_for_bb(G):
#     G_df = nx.to_pandas_edgelist(G)
#     G_df.columns = ('src', 'trg', 'nij')
#     G_df = bb.make_symmetric(G_df)
#     return G_df

def testing(df):
    return None
