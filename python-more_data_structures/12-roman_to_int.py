#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, int):
        return 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    rom = [0] * len(roman_string)
    for x in range(len(roman_string)):
        for r in dic:
            if roman_string[x] == r:
                rom[x] = dic.get(r)
    val = rom[0]
    for s in range(1, len(rom)):
        if rom[s] > rom[s - 1]:
            val = val - rom[s - 1] - rom[s - 1]
        val = val + rom[s]
    return val
