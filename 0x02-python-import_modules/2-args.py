#!/usr/bin/python3
if __name__ == "__main__":
    import sys
args_number = len(sys.argv) - 1
if args_number <= 1:
    if args_number == 1:
        print("1 argument:")
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("0 argument.")
else:
    print("{} arguments:".format(args_number))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
