import fileManagement as fm

def step_choice():
    print('Which step do you want to run?\n'+
    '\'ps\' for only projection step\n'+
    '\'bbs\' for only projection step\n'+
    '\'ds\' for only discovery step\n'+
    '\'pr\' for only print step\n'+
    '\'all\' for all the steps\n')
    choices = ['ps','bbs','ds','pr','all']
    choice = input()

    if choice in choices:
        return choice
    else :
        print('Wrong in put! Try again.')
        step_choice()

def choose_origin_file():

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
        print('Wrong input! Try again!')
        choose_projection()

def choose_node_type():
    print('On which type of nodes do you want to make the projection? \n'+
    '\'c\' for projection only on customers\n'+
    '\'q\' for projection only on queries\n'+
    '\'b\' for projection on both\n')
    choice = input()
    if choice == 'c' or choice == 'q' or choice == 'b':
        return choice
    else:
        print('Wrong input! Try again!')
        choose_node_type()
