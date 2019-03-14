import libraries.backboning as bb
import fileManagement as fm

def backboningStep():
    dataframe = fm.edgelistIntoMemory()

    # Your code here

    fm.backboningToCsv(dataframe)
