#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    zor1 = tuple_a + (0, 0)
    zor2 = tuple_b + (0, 0)
    zor = (zor1[0] + zor2[0], zor1[1] + zor2[1])
    return zor
