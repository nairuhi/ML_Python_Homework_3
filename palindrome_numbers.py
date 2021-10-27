#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:53:04 2021

@author: nairuhi
"""


def reverse (num):
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num //= 10
    return result


def is_palindrome (num):
    return num == reverse(num)


a = int(input())
b = int(input())

for i in range(a, b+1):
    if is_palindrome (i):
        print(i)
    
    