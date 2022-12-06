#Problem Link : https://www.hackerrank.com/challenges/flipping-bits/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
def flip(n):
    result = 0
    k = 1

    for _ in range(32):
        if n & 1 == 0:
            result += k

        k <<= 1
        n >>= 1

    return result


def main():
    queries = int(input())

    for _ in range(queries):
        n = int(input())
        print(flip(n))


if __name__ == '__main__':
    main()
