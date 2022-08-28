#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == len(tuple_b):
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return (tuple_c)
    elif len(tuple_a) == len(tuple_b) + 1:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1])
        return (tuple_c)
    else:
        return (tuple_a)
