import fileManagement as fm
import backboningStep as bbs
import projetionStep as ps
import discoveryStep as ds
import print as pr
import interface as intr

def main():
    argument = intr.step_choice()

    if argument == "all":

        projection()

        bbs.backboningStep()

        ds.discoveryStep()

        pr.printStep()
    elif argument == "ps":
        projection()

    elif argument == "bbs":
        bbs.backboningStep()

    elif argument == "ds":
        ds.discoveryStep()

def projection():
        intr.choose_origin_file()
        projection_type = intr.choose_projection()
        node_type = intr.choose_node_type()
        if type(projection_type) == type([1]):
            for projection in projection_type:
                ps.projetionStep(projetion,True,node_type)
        else:
            ps.projetionStep(projection_type,True,node_type)
if __name__ == '__main__':
    main()
