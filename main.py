import fileManagement as fm
import backboningStep as bbs
import projetionStep as ps
import discoveryStep as ds



def main():

    ps.projetionStep(edgelistFile = "toy_data.txt")

    bbs.backboningStep()

    ds.discoveryStep()


    #profit("?")

if __name__ == '__main__':
    main()
