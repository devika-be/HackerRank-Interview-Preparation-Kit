#Problem Link : https://www.hackerrank.com/challenges/castle-on-the-grid/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

from collections import deque


def min_moves(grid, start_x, start_y, goal_x, goal_y):
    queue = deque()
    queue.appendleft((start_x + 1, start_y + 1, 0))

    while queue:
        x, y, steps = queue.pop()
        grid[x][y] = False

        if x == goal_x + 1 and y == goal_y + 1:
            return steps

        d = 1
        while grid[x][y - d]:
            queue.appendleft((x, y - d, steps + 1))
            d += 1

        d = 1
        while grid[x + d][y]:
            queue.appendleft((x + d, y, steps + 1))
            d += 1

        d = 1
        while grid[x][y + d]:
            queue.appendleft((x, y + d, steps + 1))
            d += 1

        d = 1
        while grid[x - d][y]:
            queue.appendleft((x - d, y, steps + 1))
            d += 1


def main():
    n = int(input())
    grid = [[False] * (n + 2) for _ in range(n + 2)]

    for i in range(1, n + 1):
        row = list(map(lambda x: x == '.', input()))
        grid[i][1:-1] = row

    start_x, start_y, goal_x, goal_y = map(int, input().split())
    print(min_moves(grid, start_x, start_y, goal_x, goal_y))


if __name__ == '__main__':
    main()
