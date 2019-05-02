# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:48:01 2019

@author: ak
"""
print('hello world!!')

my_height = 172 # inches
my_weight = 84 # kgs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Brown'


print ('that\'s  too nice of you.')
print ("He's an indian")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth\tare usually \n %s \n depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d and %d I get %d." % (
    my_height, my_weight, my_height + my_weight))

#function overloading
print('hi'+' welcome') #concatenates 2 strings
print(10+20)

print('hi' * 10) #prints hi 10 times


print ("He's got {} eyes and {} hair.".format(my_eyes, my_hair))