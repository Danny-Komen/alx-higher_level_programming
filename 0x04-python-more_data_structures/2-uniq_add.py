#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new_list = []
    for i in range(len(my_list)):
        if new_list.count(my_list[i]) == 0:
            new_list.append(my_list[i])
            sum += my_list[i]
    return (sum)
 