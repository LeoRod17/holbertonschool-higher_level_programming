def print_list_integer(my_list=[]):
    txt = "{}"
    if my_list == 0:
        return -1
    size = len(my_list)
    for x in range(size):
        print(txt.format(my_list[x]))