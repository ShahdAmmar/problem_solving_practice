#!/usr/bin/python3
"""
Problem: Given a list of students with their grades, find and print the name(s)
         of the student(s) with the second lowest grade.
Source: HackerRank
"""
n = int(input("Enter the number of students: "))
students_data = []

for _ in range(n):
    name = input(f"Enter student {_+1} name: ")
    score = float(input(f"Enter student {_+1} score: "))
    students_data.append([name, score])

unique_scores = sorted({s[1] for s in students_data})
sec_low_score = unique_scores[1]

students_with_sec_low_score = [s[0] for s in students_data if s[1] == sec_low_score]
students_with_sec_low_score.sort()
for s in students_with_sec_low_score:
    print(s)