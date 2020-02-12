#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:45:11 2020

@author: nia
"""

a=[3,23,4,1,3,4,6,87,9,3,2,4,4,63,78,3,34,56,3,4,1]


num=0
swapCount=0

while True:
    for i in range(num+1,len(a)):
        if(a[num]>a[i]):
            tmp=a[num]
            a[num]=a[i]
            a[i]=tmp
            swapCount=+1
    if swapCount==0:
        break
    num+=1
    swapCount=0

print(a)
        
            
    