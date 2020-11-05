# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Level 1 Katas

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com

Excercise 3

Exercise: Draw a square
Write a function, name it square. It takes in an integer and then prints out a square using the hash character.

eg square(2) should output

##
##
eg square(4) should output

####
####
####
####

"""
def square(x):
    y = x//2
    row = ('#'*(y)) 
    line_break =  row +'\n' 
    square_ = (row + line_break)
    return square_*(x)


print(square(2))
print(square(4))
print(square(6))
print(square(8))
print(square(10))
