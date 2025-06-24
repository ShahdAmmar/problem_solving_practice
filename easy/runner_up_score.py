#!/usr/bin/python3
"""
Problem: Find Runner-Up Score (second maximum score)
Source: HackerRank
"""

n = int(input('Enter number of scores: '))
scores = map(int, input('Enter the list of scores seperated by sapce: ').split())

maximum = sec_maximum = float('-inf')

for score in scores:
    if score > maximum:
        sec_maximum = maximum
        maximum = score
    elif maximum > score > sec_maximum:
        sec_maximum = score
print(f'Runner-Up Score: {sec_maximum}')
