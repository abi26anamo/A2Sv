#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    prefix_sum = [0]*(n+1)
    for query in queries:
        prefix_sum[query[0]-1]+=query[2]
        prefix_sum[query[1]]-=query[2]
        
    running_sum = prefix_sum[0]
    max_val = prefix_sum[0]
    for i in range(1,len(prefix_sum)):
        running_sum+=prefix_sum[i]
        max_val = max(max_val,running_sum)
    return max_val
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

