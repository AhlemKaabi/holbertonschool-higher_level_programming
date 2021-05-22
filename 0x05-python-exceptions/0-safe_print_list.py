#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for elem in range(x):
            print("{}".format(my_list[elem]), end="")
            i += 1
        print("")
    except Exception:
        print("")
    return i
