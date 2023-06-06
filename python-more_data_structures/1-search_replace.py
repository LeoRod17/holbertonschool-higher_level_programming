#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if (my_list):
        for x in range(0, len(my_list)):
            if my_list[x] == search:
                my_list[x] = replace
