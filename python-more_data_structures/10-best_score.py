#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary != None):
        v = a_dictionary.values()
        m = max(v)
        for x in a_dictionary:
            if (m == a_dictionary.get(x)):
                return x
        return None
    return None
