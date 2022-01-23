# https://www.hackerrank.com/challenges/python-print/problem
# Print a Function

# The included code stub will read an integer, n, from STDIN.
# Without using any string methods, try to print the following: 123...n
# Note that "..." represents the consecutive values in between.

def function(n):
    for i in range(1, n + 1):
        print(i, end = "")
n = int(input())
function(n)

def function(n):
    for i in range(1, n + 1):
        print(i, end = " ")
n = int(input())
function(n)

def function(n):
    for i in range(1, n + 1):
        print(i, end = "-")
n = int(input())
function(n)

def function(n):
    for i in range(1, n + 1):
        print(i, end = "#")
n = int(input())
function(n)
