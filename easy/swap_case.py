#!/usr/bin/python3
"""
Problem: Given a string, convert all lowercase letters to uppercase letters
         and vice versa.
         Constraint: 0 < len(s) <= 1000
Source: HackerRank
"""

def swap_case(s):
    modified_s = ""

    if 0 < len(s) <= 1000:
        for ch in s:
            if ch.islower():
                modified_s += ch.upper()
            else:
                modified_s += ch.lower()
    else:
        print("Note: length of string should be more "
              "than 0 and lower than or equal to 1000.")

    return modified_s


if __name__ == '__main__':
    s = input("Enter the string: ")
    result = swap_case(s)
    print(result)
