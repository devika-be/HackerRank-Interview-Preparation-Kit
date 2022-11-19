#Problem Link : https://www.hackerrank.com/challenges/poisonous-plants/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def main():
    _ = int(input())
    plants = list(map(int, input().split()))
    plants.append(-1)
    answer = 0

    stack = []
    for i, plant in enumerate(plants):
        days = 1
        while stack and stack[-1][0] >= plant:
            days = max(days, stack[-1][1] + 1)
            stack.pop()

        if not stack:
            days = -1

        answer = max(answer, days)
        stack.append((plant, days))

    print(answer)


if __name__ == '__main__':
    main()
