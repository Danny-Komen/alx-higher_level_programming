#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    original = my_list[:]
    for i in range(len(original)):
        if (original[i] % 2) == 0:
            original[i] = True
        else:
            original[i] = False
    return(my_list)
