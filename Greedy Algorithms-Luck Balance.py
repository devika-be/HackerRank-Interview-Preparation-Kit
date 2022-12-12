#Problem Link : https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def main():
    n, k = map(int, input().split())
    acc = 0
    lucks = []

    for _ in range(n):
        luck, important = map(int, input().split())
        if not important:
            acc += luck
        else:
            lucks.append(luck)

    lucks.sort()

    if k == 0:
        print(acc - sum(lucks))
    else:
        print(acc + sum(lucks[-k:]) - sum(lucks[:-k]))


if __name__ == '__main__':
    main()
