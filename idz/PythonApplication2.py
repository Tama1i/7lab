#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':

    a = list(map(float, input().split()))
    v=list(enumerate(a))
    k = 0
    k1 = 0
    s = 0
    s1 = 0
    i = 0
    in1 = int(input("interval 1 "))
    in2 = int(input("interval 2 "))

    for i, val in enumerate(a):
        if abs(val) > k:
            k = abs(val)
            k1 = i
        if s == 1:
            s1 += val
        if i > 0:
            s = 1
    k = 0 

    print(f"sum = {s1}    nom = {k1}")
    b = [i for i in a if i >= in1 and i <= in2 ]
    c = [i for i in a if i < in1 or i > in2 ]

    print(b,c)
