#!/bin/python

def max_integer(my_list=[]):
    highest = 0
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if i > highest:
                highest = i

        if highest == 0:
            return(my_list[0])
        else:
            return highest
