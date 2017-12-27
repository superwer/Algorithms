#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
different powersets

"""

l = [1,2,3]

def powerset(xs):
    result = [[]]
    for x in xs:
        newsubsets = [subset + [x] for subset in result]
        result.extend(newsubsets)
    return result

print (powerset(l))
#[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

def powerset2(orig, newset):
    if orig == []:
        return [newset]
    else:
        result = []
        for s in powerset2(orig[1:], newset+[orig[0]]):
            result.append(s)
        for s in powerset2(orig[1:], newset):
            result.append(s)
        return result
print (powerset2(l,[]))
#[[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]

def powerset3(orig,newset):
    if orig == []:
        yield newset
    else:
        
        for s in powerset3(orig[1:],newset+[orig[0]]):
            yield s
        for s in powerset3(orig[1:],newset):
            yield s
print (list(powerset3(l,[])))

def powerset4(lst):
    if len(lst) <=1:
        yield lst
        yield []
    else:
        for x in powerset4(lst[1:]):
            yield[lst[0]]+x
            yield x

print (list(powerset4(l)))
#[[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]

def powerset5(lst):
    if lst == []:
        yield []
    else:
        for x in powerset4(lst[1:]):
            yield[lst[0]]+x
            yield x
            
print (list(powerset5(l)))  
#[[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]


def powerset6(lst):
    pairs = [(2**i,x) for i, x in enumerate(lst)]
    for i in range(2**len(pairs)):
        yield [x for (mask,x) in pairs if i & mask]

print (list(powerset6(l)))   
#[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]      








    
    
    
    
    
    
    
    
    
    
    
    
    
    
    











