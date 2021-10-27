#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:34:09 2021

@author: nairuhi
"""

from math import sqrt

def is_prime (n):
    for factor in range (2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True

n = int(input())


for p1 in range(2, n-1):
    if is_prime(p1):
        p2 = n - p1
        if is_prime(p2):
            print(p1, p2)
            break
        