# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:47:29 2019

@author: ak
"""

from python_functions import add, add_r, multi_add

c=add(100,200) 
d=add_r(100,200)
type(c)
type(d)
add(100)#function calling with default parameter

help(add_r)


#calling function with multiple arguments
multi_add(100,200,300)
multi_add(250,650,85,954)

