def print_list_integer(my_list=[]):
    txt = "{}"
    size = len(my_list)
    for x in range(size):
        print(txt.format(my_list[x]))
