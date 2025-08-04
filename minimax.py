#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr=arr.sort
    mini,max=0
    for i in range(len(arr)-1):
        mini+=arr[i]
    for i in range(1,len(arr)):
        max+=arr[i]
    print(mini,max)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)