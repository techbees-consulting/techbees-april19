# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:19:18 2019

@author: ak
"""
"""
1. syntax errors
2. exceptions
A Python exception is an error that’s detected during execution. 

"""

def devide(a=1,b=1):
    a= input('enter first number')
    b= input('enter second number')
    print(int(a)/int(b))
    print('stmt2')
    print('stmt3')

devide()

        
        
def devide1(a=1,b=1):
    a= input('enter first number')
    b= input('enter second number')
    try:
        print(int(a)/int(b))
    except:
        print('you can\'t devide by zero')


devide1()

def fn_multi(a=1,b=0):
    try:
        print(a/b)
        print("This won't be printed")
        print('10'+10)
    except TypeError:
        print("You added values of incompatible types")
    except ZeroDivisionError:
        print("You divided by 0")


try:
    print('hello')
except ValueError:
    print("This is a value error")
except ZeroDivisionError:
    print("You divided by 0")
finally:
    print("This will print no matter what.")
        

def devide1(a=1,b=1):
    a= input('enter first number')
    
    try:
        b= input('enter second number')
        if b==0:
            raise ZeroDivisionError
        print(int(a)/int(b))
    except ZeroDivisionError:
        print('you can\'t devide by zero')