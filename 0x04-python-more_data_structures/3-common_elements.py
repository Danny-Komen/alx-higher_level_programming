#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_1 = list(set_1)
    set_2 = list(set_2)
    common_list = []
    for i in range(len(set_1)):
        if set_1[i] in set_2:
            common_list.append(set_1[i])
    return (common_list)
