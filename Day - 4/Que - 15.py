"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program: 9

Then, the output should be: 11106
"""

sequence = input()

formula = int(sequence) + int(2*sequence) + int(3*sequence) + int(4*sequence)

print(formula)