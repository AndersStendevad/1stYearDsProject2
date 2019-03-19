import fileManagement as fm
import backboningStep as bbs
import projetionStep as ps
import discoveryStep as ds
import print as pr


def main():
    argument = input("write ps , bbs, ds, pr ,all \n")
    if argument == "all":

        ps.projetionStep()

        bbs.backboningStep()

        ds.discoveryStep()

        pr.printStep()

    elif argument == "ps":
        ps.projetionStep()

    elif argument == "bbs":
        bbs.backboningStep()

    elif argument == "ds":
        ds.discoveryStep()

    elif argument == "pr":
        pr.printStep()

if __name__ == '__main__':
    main()
