#Problem Link : https://www.hackerrank.com/challenges/find-the-nearest-clone/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
from collections import defaultdict, deque


def solve(n, g, color, color_to_analyze):
    queue = deque()
    length = [-1] * (n + 1)
    visited = [False] * (n + 1)

    for v in range(1, n + 1):
        if color[v] == color_to_analyze:
            length[v] = 0
            queue.appendleft(v)

    while queue:
        v = queue.pop()
        visited[v] = True

        for u in g[v]:
            if not visited[u]:
                if length[u] != -1:
                    return length[v] + length[u] + 1
                else:
                    length[u] = length[v] + 1
                    queue.appendleft(u)

    return -1


def main():
    n, m = map(int, input().split())
    g = defaultdict(set)

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].add(v)
        g[v].add(u)

    color = [0] * (n + 1)
    color[1:] = list(map(int, input().split()))
    color_to_analyze = int(input())

    print(solve(n, g, color, color_to_analyze))


if __name__ == '__main__':
    main()
