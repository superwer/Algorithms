#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 22:05:41 2017

@author: andreyzhilyakov
"""

#list comprehension
'''
[expr for val in collection]
[expr for val in collection if <test> ]
[expr for val in collection if <test1> and <test2>]
[expr for val in collectionq1 and val2 in collection2]
'''
#regular way
#square = []
#for i in range(1,101):
#    square.append(i**2)
##list comprehension
#square2 = [i**2 for i in range(1,101)]
#
#gmovies = [title for title in movies if title.startwith("G")]
#
#
##for tuples (title,year)
#movies = [('movie#1',2000),('movie#2',2005),('movie#3',2004)]
#pre2k = [title for (title,year) in movies if year < 2000]
#
##multiply each element of the list by a number 4:
#v=[2,3,4,5]
#w = [4*x for x in v]
##cartesian product
#A = [1 ,3, 5, 7]
#B = [2, 4, 6, 8]
#
#cartesian_product = [(a,b) for a in A for b in B]

#regular
nums = [1,2,3,4,5,6,7,8,9,10]
#new = []
#for i in nums:
#    new.append(i)
#print(new)
##list comprehension
#new1 =[i for i in nums]
#print(new1)
#
#'''
#I want n*n for each n in nums
#for n in nums:
#    new_list.append(n*n)
#'''
#new2 = [n*n for n in nums]
#print(new2)
#'''
#I want n for each n in nums if n is even
#'''
#new3=[n for n in nums if n%2==0]
#print(new3)

#using a map + lambda
#my_list = map(lambda n: n*n, nums)
#print(my_list)

#I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
#list_of_products=[(letter,num) for letter in 'abcd' for num in '0123']
#print((list_of_products))

#dictionary comprehension
#names = ['bruce','clark','peter','logan','wade']
#heros = ['batman','superman','spiderman','wolverine','deadpool']
##print (zip(names,heros))
#
##my_dict = {}
##for name, hero in zip(names,heros):
##    my_dict[name] = hero
##print(my_dict)
#
#my_dict= {name:hero for name, hero in zip(names,heros) if name !='peter' }
#
#print(my_dict)
#

#Set Comprehensions
#nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
#my_set = set()
#for i in nums:
#    my_set.add(i)
#print (my_set)

#my_set = {n for n in nums}
#print(my_set)

#Generator Expressions
#I want to yield 'n*n' for each 'n' in nums
#def gen_func(nums):
#    for n in nums:
#        yield n*n
#my_gen = gen_func(nums)

#my_gen = (n*n for n in nums)
#for i in my_gen:
#    print (i)
#my_nums = (n*n for n in [1,2,3,4])
#castin generator to a list
#print list(my_nums)


















































