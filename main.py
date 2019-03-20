import fileManagement as fm
import backboningStep as bbs
import projetionStep as ps
import discoveryStep as ds
import print as pr
import interface as intr

def main():
    argument = intr.step_choice()

    if argument == "all":

        projection_name = projection()

        backboning(projection_name)

        ds.discoveryStep()

        pr.printStep()

    elif argument == "ps":
        projection()

    elif argument == "bbs":
        backboning(projection)

    elif argument == "ds":
        ds.discoveryStep()

    elif argument == "pr":
        ds.printStep()

def projection():
        intr.choose_origin_file()
        projection_type = intr.choose_projection()
        projection_name = projection_type
        node_type = intr.choose_node_type()
        if type(projection_type) == type([1]):
            for projection in projection_type:
                ps.projetionStep(projection,True,node_type)
                projection_name = projection
        else:
            ps.projetionStep(projection_type,True,node_type)
        return projection_name

def backboning(projection_name):
    backboning_type = intr.choose_backboning()
    if type(backboning_type) == type([1]):
        for backboning in backboning_type:
            bbs.backboningStep(backboning_type = backboning, projection = projection_name)
    else:
        bbs.backboningStep(backboning_type = backboning_type, projection = projection_name)

if __name__ == '__main__':
    main()
