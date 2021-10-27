#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:08:52 2021

@author: nairuhi
"""

n = int(input())
k = int(input())

seq = [int(i) for i in input().split()]

k = k % n

print(seq[-k:] + seq[:-k])
