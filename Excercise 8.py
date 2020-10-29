# -*- coding: utf-8 -*-
"""
Umuzi Data Engineering Level 1 Katas

@author: Simphiwe Shongwe
@Git: S1mp41w3
@E-mail: Sim01Shongwe@gmail.com

Excercise 8

Exercise: Frame some text
Write a function that takes a list of strings an prints them, 
one per line, in a rectangular frame.

""" 

def frame(*words):
    border_ = max(len(word) for word in words)
    print('*' * (border_ + 4))
    for word in words:
        print('* {:<{}} *'.format(word, border_))
    print('*' * (border_ + 4))

print(frame("I am","an","Umuzi","Data","Engineering","Recruit"))