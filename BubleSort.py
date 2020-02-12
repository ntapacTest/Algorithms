#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 08:54:29 2020

@author: nia
"""

a=[1,23,4,1,3,4,6,87,9,3,2,4,4,63,78,3,34,56,3,4]

for i in range(len(a)):
    
    key=a[i]
    for j in range(0,len(a)-i-1):
        if a[j]>a[j+1]:
            t=a[j+1]
            a[j+1]=a[j]
            a[j]=t
        
print(a)
