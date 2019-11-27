#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:31:50 2019

@author: raghu
"""

def aMulB(a,b):
    if b == 1:
        return a
    else:
        return a + aMulB(a,b-1)
        
print(aMulB(3,4))

def Factorial(n):
    if n == 1:
        return 1
    else:
     return n*Factorial(n-1)
 
print(Factorial(5))
    