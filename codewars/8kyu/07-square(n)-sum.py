# DATE: 17 OCT 2026

""" Complete the square sum function so that it squares each number passed into it and then sums the results together. """

def square_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number ** 2
    return total
