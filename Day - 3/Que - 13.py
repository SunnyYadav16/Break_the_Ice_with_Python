"""
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:
hello world! 123

Then, the output should be:
LETTERS 10
DIGITS 3
"""

sequence = input()
number_of_letter = 0
number_of_digits = 0

for i in range(len(sequence)):
    if sequence[i].isalpha():
        number_of_letter += 1
    elif sequence[i].isnumeric():
        number_of_digits += 1

print(f"Letters {number_of_letter}")
print(f"DIGITS {number_of_digits}")