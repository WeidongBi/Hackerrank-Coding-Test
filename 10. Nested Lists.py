# https://www.hackerrank.com/challenges/nested-list/problem
# Nested Lists

# Given the names and grades for each student in a class of N students, store them in a nested list
# and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade,
# order their names alphabetically and print each name on a new line.

n = int(input())
grade_sheet = []
grade_list = []
for i in range(n):
    name = input()
    grade = float(input())
    record = [name, grade]
    grade_sheet.append(record)
    grade_list.append(grade)
grade_sheet.sort()
# print(grade_sheet)
# print(grade_list)
second_lowest_grade = sorted(set(grade_list))[1]
for i, j in grade_sheet:
    if j == second_lowest_grade:
        print(i)