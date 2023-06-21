#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = my_list[:]
    if 0 <= idx < len(my_list):
        a[idx] = element
        return(a)
    return(my_list)
