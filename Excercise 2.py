# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Level 1 Katas

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com

Excercise 2

Exercise: check if a number is even
Write a function named even_or_odd or evenOrOdd. 
Your function should take an integer and print in the work “even” or “odd”

Please be careful what name you choose to use. Different programming languages have different conventions.

eg, if the input is 3 then the output is “odd”. If the input is 4 then the output is “even”

"""

def even_or_odd(x):
    if x % 2:
        return str('odd')
    else:
        return str('even')
    
print(even_or_odd(2))
print(even_or_odd(3))
print(even_or_odd(0))
print(even_or_odd(66))
print(even_or_odd(33.3))


