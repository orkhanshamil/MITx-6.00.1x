""" Problem 1
10.0/10.0 points (graded)

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5"""
count = 0
for letter in s:
    if str(letter) == 'a' or str(letter) == 'e' or str(letter) == 'i' or str(letter) == 'o' or str(letter) == 'u':
        count += 1

print(count)