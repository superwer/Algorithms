#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:30:35 2017

@author: andreyzhilyakov
"""
import math
import time

def is_prime_v1(n):
    '''Return 'True' if 'n' is a prime number. False otherwise.'''
    if n == 1:
        return False #1 is not prime it is something called unit
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def is_prime_v2(n):
    '''removing duplicate products'''
    if n == 1:
        return False
    max_devisor = math.floor(math.sqrt(n))
    for i in range(2,1+max_devisor):
        if n % i == 0:
            return False
    return True
#in version 3 we eliminate even numbers
def is_prime_v3(n):
    '''removing duplicate products and even numbers'''
    if n == 1:
        return False
    #if it's even and not 2 then it's not a prime
    if n==2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_devisor = math.floor(math.sqrt(n))
    for i in range(3,1+max_devisor,2):
        
        if n % i == 0:
            return False
    return True
#======Test Function=============
t0 = time.time()
for n in range(1,100000):
    is_prime_v1(n)
t1 = time.time()
print('Time required: ', t1 - t0)
    
    
    
    
    
    
    
    