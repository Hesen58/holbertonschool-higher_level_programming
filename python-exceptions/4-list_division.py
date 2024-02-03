#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    zor = []
    for i in range(list_length):
        try:
            zor.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            zor.append(0)
        except ZeroDivisionError:
            print("division by 0")
            zor.append(0)
        except IndexError:
            print("out of range")
            zor.append(0)
        finally:
            continue
    return zor
