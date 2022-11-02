#Problem Link : https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def solve():
    s = input()
    answer = 0

    for i in range(1, len(s)):
        answer += s[i] == s[i - 1]

    return answer


def main():
    q = int(input())

    for _ in range(q):
        print(solve())


if __name__ == '__main__':
    main()
