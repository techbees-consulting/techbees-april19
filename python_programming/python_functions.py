# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:18:29 2019

@author: ak
"""
def func():
    print('func')


#function with default parameters
def add(a,b=10):
    c = a+b
    print(c)


def add_r(a,b=10):
    """this function adds \n two values"""
    c = a+b
    return c



#if you want to use parameters dynamically you can make use of args
def multi_add(*args):
    z=0;
    for a in args:
        z += a
    print('sum is {}'.format(z))
    
