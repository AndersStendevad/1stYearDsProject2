import fileManagement as fm

def printStep(freshStart=True):
    if not freshStart:
        return None
    dataframe = fm.backboningIntoMemory()
    community = fm.communityIntoMemory()
    print(dataframe.head())
