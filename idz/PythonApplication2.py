#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    a = list(map(float, input().split()))
    v=list(range(0,len(a)))
    k = 0
    k1 = 0
    s = 0
    s1 = 0
    i = 0
    in1 = int(input("interval 1 "))
    in2 = int(input("interval 2 "))

    for i in  a:
        if abs(i) > k:
            k = abs(i)
            k1 = a.index(i)
        
        if s == 1:
            s1 += i
        if i > 0:
            s = 1
    k = 0 

    print(f"sum = {s1}    nom = {k1}")
    for i in a:
        if ((i >= in1) and (i <= in2)):
            print(i," ")
        else:
            v[k] = i
            k += 1
    for i in range(0,k):
        print(" ", v[i])

   

