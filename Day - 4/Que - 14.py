"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:
Hello world!

Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

sequence = input()

upper = 0
lower = 0

for i in sequence:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print(f"UPPER CASE {upper}\nLOWER CASE {lower}")