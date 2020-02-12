#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:47:20 2020

@author: nia
"""

# Insertion sort
a=[3,1,2,5,6,2,4,2,6,9,2]

for i in range(1,len(a)):
    key=a[i]
    j=i-1
    
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key

print(a)