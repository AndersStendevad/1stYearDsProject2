import fileManagement as fm
import backboningStep as bbs
import projetionStep as ps
import discoveryStep as ds



def main():

    ps.projetionStep(freshStart = True)

    bbs.backboningStep()

    ds.discoveryStep()

if __name__ == '__main__':
    main()
