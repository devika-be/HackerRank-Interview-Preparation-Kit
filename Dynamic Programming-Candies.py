#Problem Link : https://www.hackerrank.com/challenges/candies/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = int(input())

    candies = [1] * n

    for i in range(1, n):
        if a[i] > a[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if a[i] > a[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1

    print(sum(candies))


if __name__ == '__main__':
    main()
