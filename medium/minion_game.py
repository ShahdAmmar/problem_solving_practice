#!/usr/bin/python3
"""
Problem: Kevin and Stuart are playing The Minion Game using a given string.
         Game Rules: Both players create substrings from the original string S.
                     Kevin scores a point for every substring that starts with a vowel.
                     scores a point for every substring that starts with a consonant.
         Constraint: 0 < len(S) < 10^6
Source: HackerRank
"""

def minion_game(string):
    if 0 < len(string) <= 10**6:
        vowels = ['A', 'E', 'O', 'U', 'I']
        k_score, s_score = 0, 0
        for i in range(len(string)):
            if string[i] in vowels:
                k_score += len(string) - i
            else: 
                s_score += len(string) - i
        if k_score > s_score:
            print("Kevin", k_score)
        elif s_score > k_score: 
            print("Stuart", s_score)
        else:
            print("Draw")
    else:
        raise Exception("String length should be more than 0 and less than or equal to 10^6.")  
        
                
if __name__ == '__main__':
    s = input("Enter the string: ")
    minion_game(s)