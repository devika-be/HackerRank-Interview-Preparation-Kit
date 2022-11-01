#Problem Link : https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def count(s):
    counts = [0] * 26

    for letter in s:
        counts[ord(letter) - ord('a')] += 1

    return counts


def diff(xs, ys):
    return sum(abs(x - y) for (x, y) in zip(xs, ys))


def main():
    a = input()
    b = input()
    print(diff(count(a), count(b)))


if __name__ == '__main__':
    main()
