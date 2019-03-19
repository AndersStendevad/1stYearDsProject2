import fileManagement as fm

def discoveryStep(freshStart=True):
    if not freshStart:
        return None
    dataFrame = fm.backboningIntoMemory()

    fm.communityToCsv(dataframe)
