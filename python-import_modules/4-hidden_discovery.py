#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    zor = dir(hidden_4)
    for i in zor:
        if (i[0] != "_" or i[1] != "_"):
            print("{}".format(i))
