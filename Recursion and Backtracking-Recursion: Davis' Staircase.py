#Problem Link : https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

MOD = 10000000007


def solve(n):
    dp = [0] * max(3, n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = dp[1] + dp[0]

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

    return dp[n]


def main():
    s = int(input())
    for _ in range(s):
        n = int(input())
        print(solve(n))


if __name__ == '__main__':
    main()
