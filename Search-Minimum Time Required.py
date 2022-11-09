#Problem Link : https://www.hackerrank.com/challenges/minimum-time-required/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

def count(machines, days):
    return sum(map(lambda x: days // x, machines))


def main():
    n, goal = map(int, input().split())
    machines = list(map(int, input().split()))

    lower = 0
    upper = goal * min(machines)

    while lower < upper:
        middle = (lower + upper) // 2
        if count(machines, middle) >= goal:
            upper = middle
        else:
            lower = middle + 1

    print(lower)


if __name__ == '__main__':
    main()
