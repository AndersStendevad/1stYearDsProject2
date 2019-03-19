import libraries.backboning as bb
import networkx as nx
import fileManagement as fm
import print as pr

def backboningStep(backboning_type="noise_corrected",freshStart=True):
    if freshStart == False:
        return None

    dataframe = fm.projetionIntoMemory()

    pr.cprint('Started '+backboning_type+' backboning')
    bb_df = backboning(dataframe,backboning_type)

    bb_df = bb.thresholding(bb_df,float(input("How about you pick a threshold for removing shit \n")))

    print("stability_jac = ",bb.stability_jac(dataframe, bb_df))
    print("stability_corr = ",bb.stability_corr(dataframe, bb_df))

    fm.backboningToCsv(bb_df)


def printInfo(dataframe,start=0,end=10,step=1):
    pr.cprint(bb.test_densities(dataframe, start, end, step))

def naive(dataframe):
    dataframe = bb.naive(dataframe)
    printInfo(dataframe,start=0,end=10,step=1)
    return dataframe

def noise_corrected(dataframe):
    dataframe = bb.noise_corrected(dataframe)
    printInfo(dataframe,start=0,end=10,step=1)
    return dataframe

def doubly_stochastic(dataframe):
    dataframe = bb.doubly_stochastic(dataframe)
    printInfo(dataframe,start=0,end=10,step=1)
    return dataframe

def disparity_filter(dataframe):
    dataframe = bb.disparity_filter(dataframe)
    printInfo(dataframe,start=0,end=10,step=1)
    return dataframe

def high_salience_skeleton(dataframe):
    dataframe = bb.high_salience_skeleton(dataframe)
    printInfo(dataframe,start=0,end=10,step=1)
    return dataframe

def maximum_spanning_tree(dataframe):
    dataframe = bb.maximum_spanning_tree(dataframe)
    printInfo(dataframe,start=0,end=10,step=1)
    return dataframe

def backboning(dataframe,backboning_type):
    '''Returns the type of backboning'''

    if backboning_type == "naive":
        return naive(dataframe)
    elif backboning_type == "noise_corrected":
        return noise_corrected(dataframe)
    elif backboning_type == "doubly_stochastic":
        return doubly_stochastic(dataframe)
    elif backboning_type == "disparity_filter":
        return disparity_filter(dataframe)
    elif backboning_type == "high_salience_skeleton":
        return high_salience_skeleton(dataframe)
    elif backboning_type == "maximum_spanning_tree":
        return maximum_spanning_tree(dataframe)

    else:
        print("There is no backboning type: " + backboning_type )
        print('The backboning types are:\n '+
        '\'naive\' for naive backboning\n'+
        '\'noise_corrected\' for noise_corrected backboning\n'+
        '\'doubly_stochastic\' for  doubly stochastic backboning\n'+
        '\'disparity_filter\' for disparity filter backboning\n'
        '\'high_salience_skeleton\' for  high_salience_skeleton backboning\n'+
        '\'maximum_spanning_tree\' for maximum spanning tree backboning\n')
