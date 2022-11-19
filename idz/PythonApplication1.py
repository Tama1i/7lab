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

    for i in  a:
        if (i % 7 == 0)  and (i < 0):
            s += i
            k += 1
    for i in a:
        print(i," ")
    print(f"sum = {s}    kolvo = {k}")
