# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 14:08:56 2023

@author: khaxa
"""

import sys
print(sys.path)
#pip install google-api-python-client
#pip install --upgrade google-api-python-client
import googleapiclient

"""
https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/
https://www.freecodecamp.org/news/time-complexity-of-algorithms/#:~:text=When%20we%20analyse%20an%20algorithm,are%20the%20number%20of%20operations).
https://stackoverflow.com/questions/9252891/big-o-what-is-the-complexity-of-summing-a-series-of-n-numbers
Name	     Big O
Constant	 O(c)
Logarithmic	 O(log(n))      Binary search (sorting is required) nlog2n
Linear	     O(n)           Linear search
Log Linear	 O(nlog(n))     Quick Sort
SumNumSeq     (n²+n)/2       Not linear, still quadratic, yet half in worst case scenario. 
Quadratic	 O(n²)          Selection Sort
Cubic	     O(n³)
Polynomial   O(n^p)
Exponential	 O(2ⁿ)
Factorial    O(n!) ~ O(nⁿ)          Travelling salesperson

"""
##########################################################
arr=[4, 5, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # list
l=arr.__len__()
print("N is (",l,")")
##########################################################
def quadratic_algo(items):
    steps=0
    for item in items:
        for item2 in items:
            steps=steps+1
    return steps
O=quadratic_algo(arr)
print("quadratic_algo has complexity if O(",O,")")
##########################################################
def interview_algo(items, target):
    steps=0
    complements=[]
    for item in items:
        #print(item)
        for c in complements:
            steps=steps+1
            #print("item: ", item, "   complement: " , c, "    steps:", steps)
            if item == c:
                return steps
        complements.append(target-item)
    return steps
O=interview_algo(arr,100)
print("interview _algo has complexity if O(",O,")")
##########################################################
def constant_algo(items):
    result = items[0] * items[3]+10000
    return result
O=constant_algo(arr)
print("constant_algo has complexity if O(",O,")")
##########################################################
def linear_algo(items):
    steps=0
    for item in items:
        #print(item)
        steps=steps+1
    return steps
O=linear_algo(arr)
print("linear_algo has complexity if O(",O,")")

