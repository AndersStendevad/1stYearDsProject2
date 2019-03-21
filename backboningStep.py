import libraries.backboning as bb
import networkx as nx
import fileManagement as fm
from os import path

def backboningStep(backboning_type="disparity_filter", projection = 'Unknown', freshStart=True):
    if freshStart == False:
        return None
    filename = fm.rawData
    out_filename = create_out_filename(backboning_type,filename,projection)
    if backboning_exists(out_filename):
        print('backboning file aready exists!')
        fm.backboningFile = out_filename
        return

    dataframe = fm.projetionIntoMemory()

    print('Started '+backboning_type+' backboning')
    bb_df = backboning(dataframe,backboning_type)
    print(printInfo(bb_df,start=0.000,end=1,step=0.025))
    bb_df = bb.thresholding(bb_df,float(input("How about you pick a threshold for removing shit \n")))

    saveBackboning(bb_df,out_filename)
    fm.backboningFile = out_filename = out_filename

def saveBackboning(bb_df,out_filename):
        fm.saveToCsv(bb_df,out_filename)
def backboning_exists(out_filename):
    return path.exists('Data/'+ out_filename)

def create_out_filename(backboning_type,origin_filename,projection):
    filename = origin_filename.split('.')[0]
    out_filename =  backboning_type + '_' + filename + '_'+projection+'.csv'
    return out_filename

def printInfo(dataframe,start=0,end=1,step=1):
    print(bb.test_densities(dataframe, start, end, step))

def naive(dataframe):
    dataframe = bb.naive(dataframe)
    printInfo(dataframe)
    return dataframe

def noise_corrected(dataframe):
    dataframe = bb.noise_corrected(dataframe)
    printInfo(dataframe)
    return dataframe

def doubly_stochastic(dataframe):
    dataframe = bb.doubly_stochastic(dataframe)
    printInfo(dataframe)
    return dataframe

def disparity_filter(dataframe):
    dataframe = bb.disparity_filter(dataframe)
    printInfo(dataframe)
    return dataframe

def high_salience_skeleton(dataframe):
    dataframe = bb.high_salience_skeleton(dataframe)
    printInfo(dataframe)
    return dataframe

def maximum_spanning_tree(dataframe):
    dataframe = bb.maximum_spanning_tree(dataframe)
    printInfo(dataframe)
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
