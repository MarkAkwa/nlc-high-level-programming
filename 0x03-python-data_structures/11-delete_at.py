#!/bin/python

def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    else:
        return my_list
    return my_list
