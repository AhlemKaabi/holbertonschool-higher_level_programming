#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        for elem in range(x):
            if isinstance(my_list[elem], int):
                print("{:d}".format(my_list[elem]), end="")
                i += 1
            else:
                elem += 1
        print("")
        return i
    except:
        return
