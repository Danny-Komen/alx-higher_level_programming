#!/usr/bin/python3
def search_replace(my_list, search, replace):
    edit_list = my_list [:]
    for i in range(len(edit_list)):
        if edit_list[i] == search:
            edit_list[i] = replace
    return (edit_list)
