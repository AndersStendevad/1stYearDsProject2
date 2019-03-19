import fileManagement as fm

def discoveryStep(freshStart=True):
    if not freshStart:
        return None
    dataframe = fm.backboningIntoMemory()

    
    fm.communityToCsv(dataframe)
