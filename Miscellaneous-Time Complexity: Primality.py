#Problem Link : https://www.hackerrank.com/challenges/ctci-big-o/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primality' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1

    return True


def main():
    p = int(input())

    for _ in range(p):
        n = int(input())
        print('Prime' if is_prime(n) else 'Not prime')


if __name__ == '__main__':
    main()
