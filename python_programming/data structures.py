# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:01:39 2019

@author: ak
"""

#List literals are written within square brackets [ ]
colors = []

colors = ['red', 'blue', 'green','yellow','cyan','pink']
print (colors[0])    
print (colors[2])
print (len(colors))


colors[2] = 'black'
for i in colors:
    print(i)

for i in range(len(colors)):
    print(colors[i])
    
j=0
while j < len(colors):
    print(colors[j])
    j += 1


li = [1,3,12,34,65]
sq_li = []
for i in li:
    i = i**2
    sq_li.append(i)

sq_li = [k**2 for k in li] #list comprehension
print(sq_li)


[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]



#Tuples

tupl = 'hi','hey','hello'
print(tupl[0])

tupl[0] = 'gm'

#set in python
li = [1,2,3,4,5,6,7,7,7]

set1 = set(li)


#dict in python
tel = {'jack': 4098, 'sape': 4139}
tel['jack']

for i in tel.items():
    print(i)

for i in tel.keys():
    print(i)

for i in tel.values():
    print(i)
