# DATE : 17 OCT 2026

""" Summation
Write a program that finds the summation of every number from 1 to num (both inclusive). 
The number will always be a positive integer greater than 0. 
Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests. """

def summation(num):
    sum = 0
    for nums in range(1, num +1):
        sum += nums
    return sum
