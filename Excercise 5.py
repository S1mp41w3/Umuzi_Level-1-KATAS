# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Level 1 Katas

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com

Excercise 5   

Exercise: Draw an isosceles triangle

"""

def isosceles(x):
    y = 1
    for i in range(1, x + 1):
        print(" " * (x-i) + "#" * y)
        y += 2
        
            
print(isosceles(20))        
print(isosceles(15))
print(isosceles(10))
print(isosceles(5))
       
           
       
    
