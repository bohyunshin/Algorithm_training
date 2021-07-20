#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arrayChallenge' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts LONG_INTEGER_ARRAY arr as parameter.
#

def arrayChallenge(arr):
    # Write your code here
    n = len(arr)
    counter = [0]*n
    for i in range(n):
        now = arr[i]
        for j in range(i-1,-1,-1):
            # print(i,j)
            left = arr[j]
            if left >= now:
                counter[i] -= abs(now-left)
            else:
                counter[i] += abs(now-left)
    return counter

