# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Level 1 Katas

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com

Excercise 7

Exercise: combine two lists/arrays
Write a function that combines two lists by alternatingly taking elements 
and prints the result

"""


     
def combine(x, y):
    ans = []
    x_index = 0; y_index = 0
    count = 0
    
    while count != len(x):
        ans.append(x[x_index]); ans.append(y[y_index])
        count += 1; x_index += 1; y_index += 1
    print(ans)

print(combine('asdfghj','1234567'))
print(combine('Limpopo','Gauteng'))

