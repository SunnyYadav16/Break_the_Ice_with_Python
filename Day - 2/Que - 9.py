"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence
capitalized.

Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

my_list = []
i = 0

while i < 2:
    x = input()
    if len(x) == 0:
        break
    my_list.append(x.upper())
    i += 1

for lines in my_list:
    print(lines)