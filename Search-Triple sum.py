#Problem Link : https://www.hackerrank.com/challenges/triple-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

def main():
    _ = input()
    xs = sorted(set(map(int, input().split())))
    ys = sorted(set(map(int, input().split())))
    zs = sorted(set(map(int, input().split())))
    count = 0

    i = 0
    j = 0

    for y in ys:
        while i < len(xs) and xs[i] <= y:
            i += 1
        while j < len(zs) and zs[j] <= y:
            j += 1

        count += i * j

    print(count)


if __name__ == '__main__':
    main()
