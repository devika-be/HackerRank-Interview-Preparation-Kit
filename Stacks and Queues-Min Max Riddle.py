#Problem Link : https://www.hackerrank.com/challenges/min-max-riddle/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict


def main():
    n = int(input())
    xs = list(map(int, input().split()))
    xs.append(-1)
    answer = [0] * n

    d, stack = defaultdict(int), []
    for i, x in enumerate(xs):
        index = i

        while stack and stack[-1][0] >= x:
            y, index = stack.pop()
            d[i - index] = max(d[i - index], y)

        stack.append((x, index))

    current = 0
    for window in range(n, 0, -1):
        current = max(current, d[window])
        answer[window - 1] = current

    print(*answer)


if __name__ == '__main__':
    main()

