import fileManipulation as fm
import backboningStep as bbs
import projetionStep as ps

def main():
    fm.fromEdgelistToPandas()

    bbs.backboningStep()

    ps.projetionStep()

    profit("?")

if __name__ == '__main__':
    main()
