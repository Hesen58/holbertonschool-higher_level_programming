#!/usr/bin/python3
for i in range(0, 100):
    if i != 99 and i < 10:
        print(f"0{i}, ")
    elif i != 99 and i > 10:
        print(f"{i}, ")
    else:
        print(f"{i}")
