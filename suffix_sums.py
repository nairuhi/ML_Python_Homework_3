#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:32:12 2021

@author: nairuhi
"""


A = [float(i) for i in input().split()]

B = []

for i in range(len(A)):
    B.append(sum(A[i:]))
print(B)
    

