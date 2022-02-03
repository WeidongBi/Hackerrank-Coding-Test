# https://www.hackerrank.com/challenges/python-lists/problem
# Lists

# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands
# where each command will be of the 7 types listed above. Iterate through each
# command in order and perform the corresponding operation on your list.

# Example:
# N = 4
# append 1
# append 2
# insert 3 1
# print
# append 1: Append 1 to the list, arr = [1]
# append 2: Append 2 to the list, arr = [1, 2]
# insert 3 1: Insert 3 at index 1, arr = [1, 3, 2]
# print: Print the array.
# output: [1, 3, 2]

# Input Format
# The first line contains an integer, n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.
# Constraints
# The elements added to the list must be integers.
# Output Format
# For each command of type print, print the list on a new line.

n = int(input())           # Can be many lines but only 7 types
list = []
for i in range(n):
    cmd = input().split()  # split(): string into a list; input 'insert 0 5'; return as a list ['insert', '0', '5']
    if cmd[0] == 'insert':
        list.insert(int(cmd[1]), int(cmd[2]))  # insert(index, value)
    elif cmd[0] == 'print':
        print(list)
    elif cmd[0] == 'remove':
        list.remove(int(cmd[1]))
    elif cmd[0] == 'append':
        list.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        list.sort()
    elif cmd[0] == 'pop':
        list.pop()
    else:
        list.reverse()


