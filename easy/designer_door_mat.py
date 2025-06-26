#!/usr/bin/python3
"""
Problem: Design a new door mat of size N x M where N is odd and M is 3 times N.
         Constraints: 5 < N < 101 and 15 < M < 303
Source: HackerRank
"""

n, m = map(int, input("For NxM door mat, enter N(odd number) and" 
                      " M(3 times N) separated by space: ").split())

if not (n % 2 == 1 and 5 < n < 101 and m == 3 * n):
    raise Exception("N should be odd number and M is 3 times N. "
                    "N should be between 5 and 101.")

mid_pattern = '.|.'
pattern_count = 1

for i in range(n):
    if i < n//2:
        middle = mid_pattern * pattern_count
        print(middle.center(m, '-'))
        pattern_count += 2
            
    elif i == n//2:
        print('WELCOME'.center(m, '-'))
            
    else:
        pattern_count -= 2
        middle = mid_pattern * pattern_count
        print(middle.center(m, '-'))