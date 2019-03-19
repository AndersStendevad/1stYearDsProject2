import fileManagement as fm

def printStep(freshStart=True):
    if not freshStart:
        return None
    dataframe = fm.backboningIntoMemory()
    community = communityIntoMemory()
    print(community)
    print(dataframe)
