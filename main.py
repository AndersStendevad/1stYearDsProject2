import fileManagement as fm
import backboningStep as bbs
import projetionStep as ps
import discoveryStep as ds


def main():
    argument = input("write ps , bbs, ds, all")
    if argument == "all":

        ps.projetionStep(freshStart = True)

        bbs.backboningStep()

        ds.discoveryStep()

    elif argument == "ps":
        ps.projetionStep(freshStart = True)

    elif argument == "bbs":
        bbs.backboningStep()

    elif argument == "ds":
        ds.discoveryStep()

if __name__ == '__main__':
    main()
