#Problem Link : https://www.hackerrank.com/challenges/pairs/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

from bisect import bisect_left


def main():
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    count = 0

    for i in range(n):
        x = a[i] + k
        position = bisect_left(a, x, i + 1)
        while position < n and a[position] == x:
            count += 1
            position += 1

    print(count)


if __name__ == '__main__':
    main()
