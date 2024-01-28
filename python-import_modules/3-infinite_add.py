#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    zor = sys.argv
    zorlen = len(sys.argv)
    zorsum = 0
    for i in range(1, zorlen):
        zorsum += int(zor[i])
    print("{}".format(zorsum))
