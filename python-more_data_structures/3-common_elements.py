#!/usr/bin/python3
def common_elements(set_1, set_2):
    for element in set_1:
        for element in set_2:
            if element in set_1 and element in set_2:
                return element
