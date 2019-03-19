import fileManagement as fm

def printStep(freshStart=True):
    if not freshStart:
        return None
    dataframe = fm.backboningIntoMemory()
    community = fm.communityIntoMemory()
    print(dataframe.sort_values(by="score", ascending=False).head())

blue = '\033[94m'
green = '\033[92m'
escape = '\033[0m'

def cprint(text, color = green):
    print(color + text + escape)
