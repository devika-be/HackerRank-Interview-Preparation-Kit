#Problem Link : https://www.hackerrank.com/challenges/making-candies/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#


def main():
    m, w, p, n = map(int, input().split())
    answer = math.ceil(n / (m * w))

    candies = 0
    passed = 0

    while True:
        left = math.ceil((n - candies) / (m * w))
        answer = min(answer, passed + left)

        if left <= 1:
            break

        if candies < p:
            required = math.ceil((p - candies) / (m * w))
            passed += required
            candies += required * m * w

        if m < w:
            m += 1
        else:
            w += 1
        candies -= p

    print(answer)


if __name__ == '__main__':
    main()
