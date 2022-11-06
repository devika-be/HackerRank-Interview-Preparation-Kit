#Problem Link : https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

from bisect import bisect_left


def main():
    trips = int(input())

    for _ in range(trips):
        money = int(input())
        n = int(input())
        flavors = sorted(zip(map(int, input().split()), range(1, n + 1)))
        costs = [f[0] for f in flavors]
        indexes = [f[1] for f in flavors]

        for left in range(n):
            right = bisect_left(costs, money - costs[left], left + 1)
            if right < n and costs[left] + costs[right] == money:
                if indexes[left] < indexes[right]:
                    print(indexes[left], indexes[right])
                else:
                    print(indexes[right], indexes[left])
                break


if __name__ == '__main__':
    main()
