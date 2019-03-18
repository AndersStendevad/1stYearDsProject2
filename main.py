import fileManagement as fm
import backboningStep as bbs
import projetionStep as ps
import discoveryStep as ds

def main():
    argument = input("write ps , bbs, ds, all \n")
    if argument == "all":

        projection()

        bbs.backboningStep()

        ds.discoveryStep()

    elif argument == "ps":
        projection()

    elif argument == "bbs":
        bbs.backboningStep()

    elif argument == "ds":
        ds.discoveryStep()

def choosefile():

    toy_filename = "toy_data.txt"
    real_filename = "ydata-ysm-advertiser-phrase-adjlist.txt"
    print('Type T if you want to work with the toy data set and R if with the real')
    choice = input()
    if choice == 'R':
        fm.rawData = real_filename
    elif choice == 'T':
        fm.rawData = toy_filename
    else:
        print('Wrong input! Try again!')
        choosefile()

def choose_projection():

    print('Your projection options are :\n'+
    '\'s\' for simple projection\n'+
    '\'h\' for hyperbolic projection\n'+
    '\'p\' for  resource allocation projection\n'+
    '\'y\' for random walks based projection\n'+
    '\'a\' to create a file for all the projections\n')
    choice = input()
    projection_types = ['simple',"hyperbolic","probs","ycn"]
    if choice == 's':
        ps.projetionStep()
    elif choice == 'h':
        ps.projetionStep(projection_type="hyperbolic")
    elif choice == 'p':
        ps.projetionStep(projection_type="probs")
    elif choice == 'y':
        ps.projetionStep(projection_type="ycn")
    elif choice == 'a':
        for i in projection_types:
            ps.projetionStep(projection_type = i)
    else:
        print('Wrong input! Try again!')
        choose_projection()

def projection():
        choosefile()
        choose_projection()

if __name__ == '__main__':
    main()
