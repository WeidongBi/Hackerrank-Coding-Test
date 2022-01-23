# https://www.hackerrank.com/challenges/list-comprehensions/problem
# List Comprehensions

# Let's learn about list comprehensions! You are given three integers x,y and z representing
# the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates
# given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here, 0 <= i <= x,
# 0 <= j <= y, 0 <= k <= z. Please use list comprehensions rather than multiple loops, as an exercise.

x = int(input())
y = int(input())
z = int(input())
n = int(input())
mylist = []                               # Create an empty list
for i in range(x + 1):                    # range(x + 1) from 0 to x
    for j in range(y + 1):                # range(y + 1) from 0 to y
        for k in range(z + 1):            # range(x + 1) from 0 to z
            if (i + j + k) != n:
                mylist.append([i, j, k])  # Append a new list to the empty list
print(mylist)