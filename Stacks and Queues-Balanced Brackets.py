#Problem Link : https://www.hackerrank.com/challenges/balanced-brackets/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

OPENING_CLOSING = {'(': ')', '[': ']', '{': '}'}


def is_balanced(brackets: str) -> bool:
    stack = []

    for bracket in brackets:
        if bracket in OPENING_CLOSING.keys():
            stack.append(bracket)
        elif len(stack) == 0 or OPENING_CLOSING[stack.pop()] != bracket:
            return False

    if len(stack) > 0:
        return False

    return True


def main():
    queries = int(input())

    for _ in range(queries):
        brackets = input()
        print('YES' if is_balanced(brackets) else 'NO')


if __name__ == '__main__':
    main()
