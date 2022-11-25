#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    a = list(map(float, input().split()))
    if len(a) != 10:
        print ("error")
        exit(1)
    k = 0
    s = 0
    i = 0

    for i,val in enumerate(a):
        if val % 7 == 0 and val < 0:
            s += val
            k += 1
  
    print(a)
    print(f"sum = {s}    kolvo = {k}")
