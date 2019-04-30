# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:47:37 2019

@author: ak
"""
#If - If Else
x = 5
y = 10
z = 20
if x > y:
    print('x is greater than y')


if x > y:
    print('x is large')
else:
    print('y is large')

if (x>y) & (x>z):
    print('x is large')
elif y>z:
    print('y is large')
else:
    print('z is large')
    




"""Iteration means executing the same block of code over and over, which can  be
 executed with loops"""
 
#while loop: indefinite iteration(number of times the loop is executed isn’t specified explicitly in advance.)
#While some condition is true do the following
cnt = 1
while cnt<10:
    print(cnt)
    cnt+=1
    
#infinite loops
while cnt>=1:
    print('print this!!')
    cnt+=1
    
#break: immediately terminates a loop entirely. 
n = 5
while n > 0:
    n = n-1
    if n == 2:
        break
    print(n)
print('Loop ended.')

#continue: immediately terminates the current loop iteration.

while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')


while n > 0:
    n -= 1
    if n == 2:
        pass
    print(n)
print('Loop ended.')

 
"""For loop: Definite iteration, in which the 
number of repetitions is specified explicitly in advance """

#simple python loop
for x in range(1,11,2):
    print(x)


for x in 'hello':
    print(x)



"""
print this:

*
**
***
****
"""
#1,2,3,4

i = 1
while i<=4:
  print ("*"*i)
  i = i+1

#Print multiplication table of 24
i = 1
m=24
while i<=10:
  print ('%d multiplies %d = %d' %(m,i,m*i))
  i = i+1

