import fileManagement as fm
import backboningStep as bbs
import projetionStep as ps
import discoveryStep as ds


def main():
    argument = input("write ps , bbs, ds, all \n")
    if argument == "all":

        ps.projetionStep()

        bbs.backboningStep()

        ds.discoveryStep()

    elif argument == "ps":
        ps.projetionStep()

    elif argument == "bbs":
        bbs.backboningStep()

    elif argument == "ds":
        ds.discoveryStep()


    #profit("?")

if __name__ == '__main__':
    main()
