#Problem Link : https://www.hackerrank.com/challenges/max-array-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    dp[0], dp[1] = a[0], max(a[0], a[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + a[i], a[i])

    print(dp[-1])


if __name__ == '__main__':
    main()
