def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10,"L": 50, "C": 100, "D": 500, "M": 1000}
    rom = roman_string
    for x in range(len(roman_string) - 1):
        for r in dic:
            if x == dic[r]:
                rom[x] = dic.get(r)
    val = rom[0]
    for s in rom:
        if rom[x] < rom[x + 1]:
            val = val - rom[x + 1]
        else:
            val = val + rom[x + 1]
    return val
