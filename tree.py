#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:43:38 2021

@author: nairuhi
"""


def tree(n):
    for i in range(1, n+1, 2):
        a = (n-i)//2
        print(" "*a, "*"*i)
    
    
n = int(input())

tree(n)

