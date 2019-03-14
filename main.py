import fileManagement as fm
import backboningStep as bbs
import projetionStep as ps



def main():

    ps.projetionStep(edgelistFile = "toy_data.txt")

    bbs.backboningStep()


    #profit("?")

if __name__ == '__main__':
    main()
