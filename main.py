import fileManagement as fm
import backboningStep as bbs
import projetionStep as ps
import discoveryStep as ds
import print as pr
import interface as intr

def main():
<<<<<<< HEAD
    argument = intr.step_choice()
=======
    argument = input("Choose <ps>, <bbs>, <ds>, <pr>, <all> \n")
    argument = input(pr.blue + "Choose <ps>, <bbs>, <ds>, <pr>, <all> \n" + pr.escape)
>>>>>>> f2afdd4cac5f2665fc5fe8ff05759bd43bef71a8

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

<<<<<<< HEAD
=======
def choosefile():

    toy_filename = "toy_data.txt"
    real_filename = "ydata-ysm-advertiser-phrase-adjlist.txt"
    pr.cprint('Type T if you want to work with the toy data set and R if with the real')
    choice = input()
    if choice == 'R':
        fm.rawData = real_filename
    elif choice == 'T':
        fm.rawData = toy_filename
    else:
        pr.cprint('Wrong input! Try again!', color = '\033[91m')
        choosefile()

def choose_projection():

    pr.cprint('Your projection options are :\n'+
    '\'s\' for simple projection\n'+
    '\'h\' for hyperbolic projection\n'+
    '\'p\' for  resource allocation projection\n'+
    '\'y\' for random walks based projection\n'+
    '\'a\' to create a file for all the projections\n')
    choice = input()
    projection_types = ['simple',"hyperbolic","probs","ycn"]
    if choice == 's':
        return 'simple'
    elif choice == 'h':
        return "hyperbolic"
    elif choice == 'p':
        return "probs"
    elif choice == 'y':
        return "ycn"
    elif choice == 'a':
        return projection_types
    else:
        pr.cprint('Wrong input! Try again!', color = '\033[91m')
        choose_projection()

def choose_node_type():
    pr.cprint('On which type of nodes do you want to make the projection? \n'+
    '\'c\' for projection only on customers\n'+
    '\'q\' for projection only on queries\n'+
    '\'b\' for projection on both\n')
    choice = input()
    if choice == 'c' or choice == 'q' or choice == 'b':
        return choice
    else:
        pr.cprint('Wrong input! Try again!', color = '\033[91m')
        choose_node_type()

>>>>>>> f2afdd4cac5f2665fc5fe8ff05759bd43bef71a8
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
