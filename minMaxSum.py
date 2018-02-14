...
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Input Format

A single line of five space-separated integers.

Constraints

Each integer is in the inclusive range .
Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
...

import sys

def miniMaxSum(arr):
    # Complete this function
    
    # to obtain the grater sum
    # Obtain the min number 
    # sum all the list, substract the min number
    min_val = min(arr)
    max_sum = sum(arr) - min_val
    
    # to obtain the smallest sum
    # Obtain the max number 
    # sum all the list, substract the max number
    max_val = max(arr)
    min_sum = sum(arr) - max_val
    
    print(str(min_sum) + ' ' + str(max_sum))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
