#Problem Link : https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def main():
    _ = int(input())
    a = sorted(map(int, input().split()))

    print(min(map(lambda x: abs(x[0] - x[1]), zip(a, a[1:]))))


if __name__ == '__main__':
    main()


