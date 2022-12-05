#Problem Link : https://www.hackerrank.com/challenges/recursive-digit-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


sys.setrecursionlimit(1000000)


def super_digit(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n


def main():
    n, k = map(int, input().split())
    print(super_digit(super_digit(n) * k))


if __name__ == '__main__':
    main()
