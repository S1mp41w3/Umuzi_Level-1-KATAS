# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Level 1 Katas

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com

Excercise 6

Exercise: find the longest string
Write a function that takes in an arra/list of strings 
and then prints out the longest one

"""


def longest(x,y,z):
    max_ = max(x,y,z,key=len) 
    return max_


print(longest('Umuzi', '123445678', 'apples' ))
print(longest('Reactive', '1643668678', 'amazing.umuzi.' ))
print(longest('Clever', '1567', 'yesterday' ))


