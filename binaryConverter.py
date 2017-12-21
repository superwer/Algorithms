#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:51:29 2017

@author: andreyZ
"""

def getBinaryRep(n, numDigits):
    '''assumes n and numDigits are non-negative ints
    return a numDigits str that is binary representation of n'''
    result = ''
    while n > 0:
        result = str(n%2) + result
        n=n//2
    if len(result) > numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits - len(result)):
        result = '0' + result
    return result

print(getBinaryRep(3,5))