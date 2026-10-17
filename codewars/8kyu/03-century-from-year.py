# DATE : 17 OCT 2026

""" Introduction
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in. """

def century(year):
    century_from_year = (year + 99) // 100
    return century_from_year
