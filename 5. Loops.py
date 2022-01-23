# https://www.hackerrank.com/challenges/python-loops/problem
# Loops

# The provided code stub reads and integer, n, from STDIN.
# For all non-negative integers i < n, print i * i.

n = int(input())
for i in range(0, n): # Range (0, n) includes 0, 1, 2, ..., (n-1)
    print(i * i)


