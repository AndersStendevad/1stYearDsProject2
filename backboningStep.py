import libraries.backboning as bb
import fileManagement as fm

def backboningStep(freshStart=True):
    if freshStart == False:
        return None

    dataframe = fm.edgelistIntoMemory()
    print(dataframe)
    # Your code here

    fm.backboningToCsv(dataframe)
