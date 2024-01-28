#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    zor = len(sys.argv)
    zoraq = zor - 1
    if zoraq == 0:
        print("{} arguments.".format(zoraq))
    elif zoraq == 1:
        print("{} argument".format(sys.argv[zoraq]))
        print("{}: {}".format(zoraq, sys.argv[zoraq]))
    else:
        print("{} arguments".format(sys.argv[zoraq]))
        for i in range(1, zor):
            print("{}: {}".format(i, sys.argv[i]))
    
