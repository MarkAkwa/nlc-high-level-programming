#!/bin/python

def add_tuple(tuple_a=(), tuple_b=()):
    in_case = ('0', '0')
    x = tuple_a + in_case
    y = tuple_b + in_case
    a = int(x[0]) + int(y[0])
    b = int(x[1]) + int(y[1])

    return(a, b)


tuple_a = (1, 89) 
tuple_b = (88, 11) 
new_tuple = add_tuple(tuple_a, tuple_b) 
print(new_tuple) 
 
print(add_tuple(tuple_a, (1, ))) 
print(add_tuple(tuple_a, ())) 
