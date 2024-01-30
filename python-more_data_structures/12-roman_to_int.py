#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (romant_sring and isinstance(roman_string, str)):
        return 0
    zorsum = 0
    zor = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    zorkey = list(zor.keys())
    zorval = list(zor.values())
    for i in range(0, len(roman_string)):
        for j in zorkey:
            if i + 1 != len(roman_string):
                if (
                    roman_string[i] == j and
                    zor[roman_string[i + 1]] <= zor[roman_string[i]]
                ):
                    zorsum += zor[j]
                elif (roman_string[i] == j
                      and zor[roman_string[i + 1]] > zor[roman_string[i]]):
                    zorsum -= zor[j]
            else:
                if roman_string[i] == j:
                    zorsum += zor[j]
    return zorsum
